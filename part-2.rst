Part 2: Building References & API docs
======================================

Concepts
********

Referencing
-----------

Another important Sphinx feature is that it allows referencing across documents.
This is another powerful way to tie documents together.

The simplest way to do this is to define an explicit reference object::

   .. _reference-name:

   Cool section
   ------------

Which can then be referenced with ``:ref:``::

   :ref:`reference-name`

Which will then be rendered with the title of the section *Cool section*.

Semantic Descriptions and References
------------------------------------

Sphinx also has much more powerful semantic referencing capabilties,
which knows all about software development concepts.

Say you're creating a CLI application. 
You can define an option for that program quite easily::

   .. option:: -i <regex>, --ignore <regex>

      Ignore pages that match a specific pattern.

That can also be referenced quite simply::

   :option:`-i`

Sphinx includes a large number of these semantic types:

* Module
* Class
* Method

External References
-------------------

Sphinx also includes a number of pre-defined references for external concepts.
Things like PEP's and RFC's::

   You can learn more about this at :pep:`8` or :rfc:`1984`.

You can read more about this in the Sphinx :ref:`inline-markup` docs.

.. _Inline Markup: sphinx-doc.org/markup/inline.html

Automatically generating this markup
------------------------------------

Of course, Sphinx wants to make your life easy.
It includes ways to automatically create these object definitions for your own code.
This is called ``audodoc``,
which allows you do to syntax like this::

   .. automodule:: crawler

and have it document the full Python module importable as ``crawler``.

.. note:: The module must be importable by Sphinx when running.
          We'll cover how to do this in the Tasks below.

You can read more about this in the Sphinx :mod:`~sphinx.ext.autodoc` docs.

Tasks
*****

Referencing Code
----------------

Let's go ahead and add a cookbook to our documentation.
Users will often come to your project to solve the same problems.
Including a Cookbook or Examples section will be a great resource for this content.

In your ``cookbook.rst``,
add the following:

.. literalinclude:: crawler/docs/step2/cookbook.rst
   :language: rst
   :linenos:

.. note::
	Live Preview: :doc:`crawler/docs/step2/cookbook`

Notice the ``:option:`` blocks here.
They are referencing a command line option for our program.

We need to go ahead and define those options.
In your ``cli.rst`` file,
add the following:

.. literalinclude:: crawler/docs/step2/cli.rst
   :language: rst
   :linenos:

.. note::
	Live Preview: :doc:`crawler/docs/step2/cli`

Here you are documenting the actual options your code takes.

Try it out
~~~~~~~~~~

Let's go ahead and build the docs and see what happens.
Do a::

	make html

Here you will see that the ``:option:`` blocks magically become links to the definition.
This is your first taste of :term:`Semantic Markup`.
With Sphinx,
we are able to simply say that something is a ``option``,
and then it handles everything for us;
linking between the definition and the usage.

Importing Code
--------------

Being able to define options and link to them is pretty neat.
Wouldn't it be great if we could do that with actual code too?
Sphinx makes this easy,
let's take a look.

We'll go ahead an create an ``api.rst`` that will hold our API reference:

.. literalinclude:: crawler/docs/step2/api.rst
   :language: rst
   :linenos:

.. note::
   Live Preview: :doc:`crawler/docs/step2/api`

Here you can see we're using the ``.. autoclass::`` directive to pull in our source code.
This will render the docstrings of your Python code nicely.

Sphinx actually imports your Python code when it does this,
so you need to make sure that it can find your code.
We'll need to add our ``PYTHONPATH`` to our ``conf.py`` so it can import the code.

.. literalinclude:: crawler/docs/step2/conf.py
   :language: py
   :lines: 18-31
   :linenos:

Try it out
~~~~~~~~~~

Now go ahead and rengerate your docs and look at the magic that happened::

	make html

Your Python docstrings have been magically imported into the project.

Tie it all together
-------------------

Now let's link directly to that for users who come in to the project.
Update your ``index.rst`` to look like:

.. literalinclude:: crawler/docs/step2/index.rst
   :language: rst
   :linenos:

.. note::
   Live Preview: :doc:`crawler/docs/step2/index`

One last time,
let's rebuild those docs::

   make html

.. warning:: You now have awesome documentation! :)

Now you have a beautiful documentation reference that is coming directly from your code.
This means that every time you change your code,
it will automatically be reflected in your documentation.

The beauty of this approach is that it allows you to keep your prose and reference documentation in the same place.
It even lets you semantically reference the code from inside the docs.
This is amazingly powerful and a great way to write documentation.

Could it get better?
In fact,
it can and it will.
Let's go on to :doc:`part-3`.

Extra Credit
************

Have some extra time left?
Let's look through the code to understand what's happening here more.

Understand the code
-------------------

A lot of the magic that is happening in :ref:`importing-code` above is actually in the source code.

Check out the code for ``crawler/main.py``:

.. literalinclude:: crawler/src/crawler/main.py
   :linenos:

As you can see,
we're heavily using RST in our docstrings.
This gives us the same power as we have in Sphinx,
but allows it to live within the code base.

This approach of having 