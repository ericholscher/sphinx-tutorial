Step 2: Building References & API docs
======================================

.. note:: Finish at 11:15

Concepts
********

Referencing
-----------

Another important Sphinx feature is that it allows referencing across documents.
This is another powerful way to tie documents together.

The simplest way to do this is to define an explicit reference object:

.. code-block:: rst

   .. _reference-name:

   Cool section
   ------------

Which can then be referenced with ``:ref:``:

.. code-block:: rst

   :ref:`reference-name`

Which will then be rendered with the title of the section *Cool section*.

Sphinx also supports ``:doc:`docname``` for linking to a document.

Semantic Descriptions and References
------------------------------------

Sphinx also has much more powerful semantic referencing capabilities,
which knows all about software development concepts.

Say you're creating a CLI application. 
You can define an option for that program quite easily:

.. code-block:: rst

   .. option:: -i <regex>, --ignore <regex>

      Ignore pages that match a specific pattern.

That can also be referenced quite simply:

.. code-block:: rst

   :option:`-i`

Sphinx includes a large number of these semantic types, including:

* :rst:dir:`Module <py:module>`
* :rst:dir:`Class <py:class>`
* :rst:dir:`Method <py:method>`

External References
-------------------

Sphinx also includes a number of pre-defined references for external concepts.
Things like PEP's and RFC's:

.. code-block:: rst

   You can learn more about this at :pep:`8` or :rfc:`1984`.

You can read more about this in the Sphinx :ref:`inline-markup` docs.

Automatically generating this markup
------------------------------------

Of course, Sphinx wants to make your life easy.
It includes ways to automatically create these object definitions for your own code.
This is called ``audodoc``,
which allows you do to syntax like this:

.. code-block:: rst

   .. automodule:: crawler

and have it document the full Python module importable as ``crawler``.
You can also do a full range of auto functions:

.. code-block:: rst

   .. autoclass::
   .. autofunction:: 
   .. autoexception:: 

.. warning:: The module must be importable by Sphinx when running.
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

.. literalinclude:: crawler/docs/step2/cookbook.txt
   :language: rst
   :linenos:

.. note::
	Live Preview: :doc:`crawler/docs/step2/cookbook`

Remember, you will need to use ``:option:`` blocks here.
This is because they are referencing a command line option for our program.

Adding Reference Targets
------------------------

Now that we have pointed at our CLI options,
we need to actually define them.
In your ``cli.rst`` file,
add the following:

.. literalinclude:: crawler/docs/step2/cli.txt
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
This is your first taste of Semantic Markup.
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

We'll go ahead and create an ``api.rst`` that will hold our API reference:

.. literalinclude:: crawler/docs/step2/api.txt
   :language: rst
   :linenos:

.. note::
   Live Preview: :doc:`crawler/docs/step2/api`

Remember, you'll need to use the  ``.. autoclass::`` directive to pull in your source code.
This will render the docstrings of your Python code nicely.

Requirements
------------

In order to build your code,
it needs to be able to import it.
This means it needs all of the required Python modules you import in the code.

If you have third party dependencies,
that means that you have to have them installed in your Python environment.
Luckily,
for most cases you can actually mock these variables using `autodoc_mock_imports <http://www.sphinx-doc.org/en/stable/ext/autodoc.html#confval-autodoc_mock_imports>`_.

In your ``conf.py`` go ahead and add:

    autodoc_mock_imports = ['bs4', 'requests']

This will allow your docs to import the example code without requiring those modules be installed.

Tell Sphinx about your code
---------------------------

When Sphinx runs autodoc,
it imports your Python code to pull off the docstrings.
This means that Sphinx has to be able to see your code.
We'll need to add our ``PYTHONPATH`` to our ``conf.py`` so it can import the code.

If you open up your ``conf.py`` file,
you should see something close to this on line 18:

.. literalinclude:: crawler/docs/step1/conf.py
   :lines: 18-21

As it notes,
you need to let it know the path to your Python source.
In our example it will be ``../src/``,
so go ahead and put that in this setting.

.. note:: You should always use relative paths here.
          Part of the value of Sphinx is having your docs build on other people's computers,
          and if you hard code local paths that won't work!

Try it out
~~~~~~~~~~

Now go ahead and regenerate your docs and look at the magic that happened::

	make html

Your Python docstrings have been magically imported into the project.

Tie it all together
-------------------

Now let's link directly to that for users who come in to the project.
Update your ``index.rst`` to look like:

.. literalinclude:: crawler/docs/step2/index.txt
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

Extra Credit
************

Have some extra time left?
Let's look through the code to understand what's happening here more.

Look through intersphinx
------------------------

Intersphinx allows you to bring the power of Sphinx references to multiple projects.
It lets you pull in references,
and semantically link them across projects.
For example,
in this guide we reference the Sphinx docs a lot,
so we have this intersphinx setting::

   intersphinx_mapping = {
       'sphinx': ('http://sphinx-doc.org/', None),
   }

Which allows us to add a prefix to references and have them resolve:

.. code-block:: rst

   :ref:`sphinx:inline-markup`

We can also ignore the prefix,
and Sphinx will fall back to intersphinx references if none exist in the current project:

.. code-block:: rst

   :ref:`inline-markup`

You can read more about this in the :mod:`~sphinx.ext.intersphinx` docs.

Understand the code
-------------------

A lot of the magic that is happening in `Importing Code`_ above is actually in the source code.

Check out the code for ``crawler/main.py``:

.. literalinclude:: crawler/src/crawler/main.py
   :linenos:

As you can see,
we're heavily using RST in our docstrings.
This gives us the same power as we have in Sphinx,
but allows it to live within the code base.

This approach of having the docs live inside the code is great for some things.
However,
the power of Sphinx allows you to mix docstrings and prose documentation together.
This lets you keep the amount of 

Moving on
---------

Could it get better?
In fact,
it can and it will.
Let's go on to :doc:`step-3`.
