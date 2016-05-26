"""
Main Module
"""
import time
from optparse import OptionParser
# Python 3 compat
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from utils import log, should_ignore


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
        if ignore:
            self.ignore = ignore.split(',')
        else:
            self.ignore = []

    def get(self, url):
        """
        Get a specific URL, log its response, and return its content.

        :param url: The fully qualified URL to retrieve
        """
        response = requests.get(url)
        log(url, response.status_code)
        return response.content

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
            if should_ignore(self.ignore, to_get):
                print('Ignoring URL: {url}'.format(url=to_get))
                continue
            self.get(to_get)
            time.sleep(self.delay)


def run_main():
    """
    A small wrapper that is used for running as a CLI Script.
    """

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", default="http://docs.readthedocs.org/en/latest/",
                      help="URL to fetch")
    parser.add_option("-d", "--delay", dest="delay", type="int", default=1,
                      help="Delay between fetching")
    parser.add_option("-i", "--ignore", dest="ignore", default='',
                      help="Ignore a subset of URL's")

    (options, args) = parser.parse_args()

    c = Crawler(url=options.url, delay=options.delay, ignore=options.ignore)
    c.crawl()

if __name__ == '__main__':
    run_main()
