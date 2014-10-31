
Step 2
======

Referencing Code
****************

Let's go ahead and add a cookbook to our documentation.
Users will often come to your project to solve the same problems.
Including a Cookbook or Examples section will be a great resource for this content.

In your ``cookbook.rst``,
add the following:

.. literalinclude:: crawler/docs/step2/cookbook.rst
   :language: rst
   :linenos:

..
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

.. 
	.. note::
		Live Preview: :doc:`crawler/docs/step2/cli`

Here you are documenting the actual options your code takes.

Let's go ahead and build the docs and see what happens.
Do a::

	make html
	open _build/html/cookbook.html

Here you will see that the ``:option:`` blocks magically become links to the definition.
This is your first taste of :term:`Semantic Markup`.
With Sphinx,
we are able to simply say that something is a ``option``,
and then it handles everything for us;
Linking between the definition and the usage.


Importing Code
**************

Being able to define options and link to them is pretty neat.
Wouldn't it be great if we could do that with actual code too?
Sphinx makes this easy,
let's take a look.

We'll go ahead an create an ``api.rst`` that will hold our API reference:

.. literalinclude:: crawler/docs/step2/api.rst
   :language: rst
   :linenos:

Here you can see we're using the ``.. autoclass::`` directive to pull in our source code.
This will render the docstrings of your Python code nicely.

Sphinx actually imports your Python code when it does this,
so you need to make sure that it can find your code.
We'll need to add our ``PYTHONPATH`` to our ``conf.py`` so it can import the code.

.. literalinclude:: crawler/docs/step2/conf.py
   :language: py
   :lines: 18-31
   :linenos:


Now go ahead and rengerate your docs and look at the magic that happened::

	make html

Your Python docstrings have been magically imported into the project.

Now let's link directly to that for users who come in to the project.
Update your ``index.rst`` to look like:

.. literalinclude:: crawler/docs/step2/index.rst
   :language: rst
   :linenos:


Now you have a beautiful documentation reference that is coming directly from your code.
This means that every time you change your code,
it will automatically be reflected in your documentation.

The beauty of this approach is that it allows you to keep your prose and reference documentation in the same place.
It even lets you semantically reference the code from inside the docs.
This is amazingly powerful and a great way to write documentation.