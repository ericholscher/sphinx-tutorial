Step 3
======

Now we have a wonderful set of documentation,
so we want to make sure it stays up to date and correct.

There are two factors here:
* The documentation is up to date with the code
* The user is seeing the latest version of the docs

We will solve the first problem with Sphinx's :doc:`doctest` module.
The second problem we will solve by deploying our docs to `Read the Docs`_.

sphinx.ext.doctest
------------------

This module is quite powerful.
It allows you to run tests against your code inside your docs.
This means that you can verify all of the code examples work,
so that your docs are always up to date with your code!

.. warning:: This only works for Python currently.

.. todo:: fix doc link

You can read the full `documentation`_,
but here is a basic example::

	>>> print "hello there"
	hello there

When you run this example,
Sphinx will validate the return is what is expected.

Let's look at a more interesting example.
Add a ``utils.rst`` module to your project that looks like:

.. literalinclude:: crawler/docs/step3/utils.rst
   :language: rst
   :linenos:

As you can see here,
we are actually testing our logic.
It also acts as documentation for your users,
and is included in the output of your documentation.

These doctests do double duty,
acting as **tests and documentation**.

Caveats
~~~~~~~

Note that we have to import our code in the ``testsetup::`` block.
This is so that Sphinx can call the functions properly in our doctest blocks.
This is hidden in the output of the docs though,
so users won't be confused.

.. note:: You can also put doctest blocks directly in your docstrings.
		  They will need to include full import paths though,
		  as Sphinx can't guarentee the ``testsetup::`` directive will be called.


Read the Docs
-------------

Last but not least,
once you've written your documentation you have to put it somewhere for the world to see!
Read the Docs makes this quite simple,
and is free for all open source projects.

* Register for an account at http://readthedocs.org
* Click the *Import Project* button
* Add the URL for a specific repository you want to build docs for
* Sit back and have a drink while Read the Docs does the rest.

It will:
	* Pull down your code
	* Install your ``requirements.txt``
	* Build HTML, PDF, and ePub of your docs
	* Serve it up online at ``http://<projectname>.readthedocs.org``

Let's see what that looks like in practice.