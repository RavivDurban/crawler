#This is Raviv and Noam's project :)

import urllib.request
import urllib.parse
import html.parser
import argparse
import yaml
import sys
import re


class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_links = []
        self.all_links = []
        self.url = ""

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if not name in ('href', 'src'):
                continue

            link = urllib.parse.urljoin(self.url, value)

            if re.search(arguments.ignore_regex, link):
                continue

            if not link in self.all_links:
                self.current_links.append(link)
                self.all_links.append(link)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--depth', type=int, default=2)
    parser.add_argument('-ir', '--ignore_regex', type=str, default="^$")
    parser.add_argument('url', type=str)
    arguments = parser.parse_args()

    HTMLparser = MyHTMLParser()


def scan_urls(url):
    try:
        HTMLparser.url = url
        HTMLparser.feed(str(urllib.request.urlopen(url).read()))
        links = HTMLparser.current_links.copy()
        HTMLparser.current_links = []
        return links
    except:
        return []


def get_web_of_links():
    result = {"root":arguments.url, "web":[{"level":i, "links":[]} for i in range(arguments.depth+1)]}
    result["web"][0]["links"] = [arguments.url]

    for i in range(arguments.depth):
        for link in result["web"][i]["links"]:
            result["web"][i+1]["links"] += scan_urls(link)

        if len(result["web"][i+1]["links"]) == 0:
            for j in range(arguments.depth, i, -1):
                result["web"].pop(j)
            break

    return result


if __name__ == "__main__":
    yaml.dump(get_web_of_links(), stream=sys.stdout)
