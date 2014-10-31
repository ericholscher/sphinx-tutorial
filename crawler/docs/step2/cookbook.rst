========
Cookbook
========

Crawl a web page
----------------

The most simple way to use our program is with no arguments.
Simply run::

	crawler <url>

to crawl a webpage.

Crawl a page slowly
-------------------

To add a delay to your crawler,
use :option:`-d`::

	crawler -d 10 <url>

This will wait 10 seconds between page fetches.

Crawl only your blog
--------------------

You will want to use the :option:`-i` flag,
which while ignore URLs matching the passed regex::

	crawler -i "^blog" <url>

This will only crawl pages that contain your blog URL.
