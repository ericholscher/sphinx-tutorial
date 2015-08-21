import re
import time
from optparse import OptionParser

try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class Crawler(object):

    """
    Main Crawler object.

    Example::

        c = Crawler('http://example.com')
        c.crawl()

    :param delay: Number of seconds to wait between searches
    :param ignore: Paths to ignore

    """

    def __init__(self, url, delay, ignore):
        self.url = url
        self.delay = delay
        self.ignore = ignore.split(',')

    def get(self, url):
        """
        Get a specific URL, log its response, and return its content.

        :param url: The fully qualified URL to retrieve
        """
        response = requests.get(url)
        print("({status}) {url} ".format(url=url, status=response.status_code))
        return response.content

    def should_ignore(self, url):
        """
        Returns True if the URL should be ignored

        :param url: The fully qualified URL to compare again
        """

        for pattern in self.ignore:
            compiled = re.compile(pattern)
            if compiled.search(url):
                return True
        return False

    def crawl(self):
        """
        Crawl the URL set up in the crawler.

        This is the main entry point, and will block while it runs.
        """
        html = self.get(self.url)
        soup = BeautifulSoup(html, "html.parser")
        for tag in soup.findAll('a', href=True):
            link = tag['href']
            parsed = urlparse(link)
            if parsed.scheme:
                to_get = link
            else:
                to_get = self.url + link
            if self.should_ignore(to_get):
                continue
            self.get(to_get)
            time.sleep(self.delay)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", default="http://docs.readthedocs.org/en/latest/",
                      help="URL to fetch")
    parser.add_option("-d", "--delay", dest="delay", type="int", default=1,
                      help="Delay between fetching")
    parser.add_option("-i", "--ignore", dest="ignore", default="",
                      help="Ignore a subset of URL's")

    (options, args) = parser.parse_args()

    c = Crawler(url=options.url, delay=options.delay, ignore=options.ignore)
    c.crawl()
