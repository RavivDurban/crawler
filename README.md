# crawler
This is Raviv's and Noam's project

The crawler only works for HTTP / HTTPS sites because of package limitations

To use the crawler type (after downloading):
  <py/python/python3> crawler.py [-d DEPTH] [-ir IGNORE_REGEX]

Depth (int) is set to 2 by default.
Ignore Regex - input is a string that repreasents a regex and the crawler discardes any url that follows the regex.