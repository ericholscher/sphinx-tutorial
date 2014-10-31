import urllib2


class Crawler(object):
    """
    Let's us crawl stuff

    Example:

    c = Crawler('http://example.com')
    c.crawl()
    """

    def __init__(self, url):
        self.url = url

    def crawl(self):
        """
        Crawl the URL set up in the crawler.

        Prints status as it goes.
        """
        response = urllib2.urlopen(self.url)
        html = response.read()
        print "Got {url}".format(url=self.url)
