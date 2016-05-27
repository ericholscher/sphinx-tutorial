Finishing Up: Additional Extensions & Individual Exploration
============================================================

If there is much time left in the session,
take some time to play around and get to know Sphinx better.
There is a large ecosystem of extensions,
and lots of builtin features we haven't covered.

I'm happy to consult with you about interesting challenges you might be facing with docs.

Part of being a good user of Sphinx is knowing what all is there.
Here are a few options for what to look at:

* :ref:`dev-extensions`
* Read through all the existing :ref:`extensions`
* `Breathe <http://breathe.readthedocs.org/en/latest/>`_
* Explore the Read the Docs Admin Panel
* Apply these docs to a project you have
* Show a neighbor what you've done & talk about the concepts learned.

Also, here are a number of more thought out examples of things you might do:

.. contents:: 
   :local:

Markdown Support
----------------

You can use Markdown and reStructuredText in the same Sphinx project.
We support this natively on Read the Docs, and you can do it locally::

    $ pip install recommonmark

Then in your ``conf.py``:

.. code-block:: python

    from recommonmark.parser import CommonMarkParser

    source_parsers = {
        '.md': CommonMarkParser,
    }

    source_suffix = ['.rst', '.md']

.. note:: Markdown doesn't support a lot of the features of Sphinx,
          like inline markup and directives.
          However, it works for basic prose content.

You can now add a Markdown file with a ``.md`` extension,
and Sphinx will build it into the project.
You can do things like include it in your normal TOC Tree,
and Sphinx will search it.

Go ahead and add a new Markdown File with an ``.md`` extension.
Since we haven't covered Markdown in this text,
here is an example ``community.md``::

    # Community Standards

    The Crawler community is quite large,
    and with that we have a specific set of standards that we apply in our community.

    All of our project spaces are covered by the [Django Community Code of Conduct](https://djangoproject.com/conduct/].

    ### Feedback

    Any issues can be sent directly to our [project mailing list](mailto:community@crawler.com).

Add it to your ``toctree`` in your ``index.rst`` as well,
and you will see it appear properly in Sphinx.

Generate i18n Files
-------------------

Sphinx has support for i18n.
If you do a ``make gettext`` on your project,
you should get a gettext catalog for your documentation.
Check for it in ``_build/locale``.

You can then use these files to translate your documentation using most standard tools.
You can read more about this in Sphinx's :ref:`sphinx:intl` doc.

Play with Sphinx autoapi
------------------------

``sphinx-autoapi`` is a tool that I am helping develop which will make doing API docs easier.
It depends on parsing,
instead of importing code.
This means you don't need to change your PYTHONPATH at all,
and we have a few other different design decisions.

First you need to install autoapi:

.. code:: bash

        pip install sphinx-autoapi

Then add it to your Sphinx project's ``conf.py``:

.. code:: python

        extensions = ['autoapi.extension']

        # Document Python Code
        autoapi_type = 'python'
        autoapi_dir = '../src'

AutoAPI will automatically add itself to the last TOCTree in your top-level ``index.rst``.

This is needed because we will be outputting rst files into the ``autoapi`` directory.
This adds it into the global TOCTree for your project,
so that it appears in the menus.

Add Django Support
------------------

Have a Django project laying around?
Add Sphinx documentation to it!
There isn't anything special for Django projects except for the ``DJANGO_SETTINGS_MODULE``.

You can set it in your ``conf.py``,
similar to ``autodoc``.
Try this piece of code::

    # Set this to whatever your settings file should default to.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.test")


Tables
------

Tables can be a tricky part of a lot of lightweight markup languages.
Luckily,
RST has some really nice features around tables.
It supports tables in a couple easier to use formats:

* `CSV <http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4>`_
* `List <http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table>`_

So for example,
you can manage your tables in Google Docs,
then export them as CSV in your docs.


An example of a CSV table:

.. code-block:: rst

    .. csv-table:: 
       :header: "Treat", "Quantity", "Description"
       :widths: 15, 10, 30

       "Albatross", 2.99, "On a stick!"
       "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
       crunchy, now would it?"
       "Gannet Ripple", 1.99, "On a stick!"

And a rendered example:

.. csv-table:: 
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

Go ahead and try it yourself!