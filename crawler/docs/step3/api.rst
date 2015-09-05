Crawler Python API
==================

Getting started with Crawler is easy.
The main class you need to care about is :class:`~crawler.main.Crawler`

crawler.main
------------

.. automodule:: crawler.main
   :members:

crawler.utils
-------------

.. testsetup:: *

   from crawler.utils import should_ignore, log

.. automethod:: crawler.utils.should_ignore

.. doctest::

	>>> should_ignore(['blog/$'], 'http://ericholscher.com/blog/')
	True

.. doctest::

	# This test should fail
	>>> should_ignore(['home'], 'http://ericholscher.com/blog/')
	True

.. automethod:: crawler.utils.log

.. doctest::

	>>> log('http://ericholscher.com/blog/', 200)
	OK: 200 http://ericholscher.com/blog/ 

.. doctest::

	>>> log('http://ericholscher.com/blog/', 500)
	ERR: 500 http://ericholscher.com/blog/

.. doctest::

	# This test should fail
	>>> log('http://ericholscher.com/blog/', 500)
	OK: 500 http://ericholscher.com/blog/

