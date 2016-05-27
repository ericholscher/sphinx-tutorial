Step 3: Keeping Documentation Up to Date
========================================

Now we have a wonderful set of documentation,
so we want to make sure it stays up to date and correct.

There are two factors here:

* The documentation is up to date with the code
* The user is seeing the latest version of the docs

We will solve the first problem with Sphinx's :mod:`~sphinx.ext.doctest` module.
The second problem we will solve by deploying our docs to `Read the Docs`_.

.. _step-3-concepts:

Concepts
********

Testing your code
-----------------

Sphinx ships with a ``doctest`` module which is quite powerful.
It allows you to run tests against your code inside your docs.
This means that you can verify all of the code examples work,
so that your docs are always up to date with your code!

.. warning:: This only works for Python currently.

You can read the full Sphinx docs for :mod:`~sphinx.ext.doctest`,
but here is a basic example:

.. code-block:: rst

	.. doctest::

		>>> sum(2, 2)
		4

When you run this example,
Sphinx will validate the return is what is expected.

If you need any other code to be run,
but not output to the user,
you can use ``testsetup``:


.. code-block:: rst

	.. testsetup::

		import os

		x = 4

This will then be available in the examples that you actually show your user.

Hosting docs on Read the Docs
-----------------------------

Read the Docs (https://readthedocs.org) is an open source doc hosting site.
It's built in Django,
and is free to use for open source projects.
It hosts Sphinx documentation,
automatically building it each time you make a commit.

Read the Docs gives you a number of additional features,
over hosting Sphinx yourself:

* You can add Versions to your project for each tag & branch.
* You can alerts for when your doc build fails
* You can search across the full set of docs with Elastic Search

We'll be putting your docs up on Read the Docs at the end of this tutorial.

Tasks
*****

Add doctests to our utils
-------------------------

The utils module is inside ``crawler`` is a good candidate for testing.
It has small,
self-contained pieces of logic that will work great as doctests.

Open your ``api.rst``, and update it to look like:

.. literalinclude:: crawler/docs/step3/api.txt
   :language: rst
   :linenos:

.. note::
   Live Preview: :doc:`crawler/docs/step3/api`

Now go ahead and add the RST markup that is covered above in the :ref:`step-3-concepts` section.

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
		  as Sphinx can't guarantee the ``testsetup::`` directive will be called.

Test your docs
--------------

You can now go ahead and test your docs::

	make doctest

.. note:: You will need to make sure to add the ``sphinx.ext.doctest`` to your ``extensions``.
	      Open up your ``conf.py`` file and make sure that you have it there.

It should provide output that looks similar to this::

	Doctest summary
	===============
	    5 tests
	    2 failures in tests
	    0 failures in setup code
	    0 failures in cleanup code
	build finished with problems.

As you can see,
some of the tests are broken!
You should go ahead and fix the tests :)

Requirements
------------

In order for Read the Docs to build your code,
it needs to be able to import it.
This means it needs all of the required Python modules you import in the code.

You can add a ``requirements.txt`` to the top-level of your project:

.. literalinclude:: requirements.txt

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



Extra Credit
************

Have some extra time left?
Let's run the code and see if it actually works!

Explore doctests more
---------------------

Sphinx's :mod:`~sphinx.ext.doctest` module has more interesting options.
You can do things that look more like normal unit tests,
as well as specific "doctest-style" testing.
Go in and re-write one of the existing tests to use the ``testcode`` directive instead of the ``doctest`` directive.

Run the crawler
---------------

Go ahead and run the crawler against the Read the Docs documentation::

	# in crawler/src/crawler
	python main.py -u https://docs.readthedocs.org/en/latest/

You should see your terminal start printing output,
if your internet if working.

Can you add another command line option,
and document it?

Moving on
---------

Now we are at the last part of our Tutorial.
Let's head on over to :doc:`finish`.