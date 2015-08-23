Getting Started: Overview & Introduction to Concepts
====================================================

Concepts
********

Sphinx Philosophy
-----------------

`Sphinx`_ is what is called a documentation generator.
This means that it takes a bunch of source files in plain text,
and generates a bunch of other awesome things, mainly HTML.
For our use case you can think of it as a program that takes in plain text
files in `reStructuredText`_ format, and outputs HTML.

::

    reST -> Sphinx -> HTML

So as a user of Sphinx, your main job will be writing these text files.
This means that you should be minimally familiar with `reStructuredText`_ as
a language.
It's similar to Markdown in a lot of ways,
if you are already familiar with Markdown.

Tasks
*****

Installing Sphinx
-----------------

The first step is installing `Sphinx`_.
Sphinx is a python project,
so it can be installed like any other python library.
Every Operating System should have Python pre-installed,
so you should just have to run::

    sudo easy_install Sphinx

.. note:: Advanced users can install this in a virtualenv if they wish.
    Also, ``pip install Sphinx`` works fine if you have Pip.

Getting Started
---------------

Now you are ready to creating documentation.
Create a directory called ``crawler``.
Inside that directory you should create a ``docs`` directory,
and move into it::
  
    mkdir crawler
    cd crawler
    mkdir docs
    cd docs

Then you can create the Sphinx project skeleton in this directory::

    sphinx-quickstart

Have the *Project name* be ``Crawler``, 
put in your own *Author name*,
and put in 1.0 be the *Project version*.
Otherwise you can accept the default options.

My output looks like this:

.. literalinclude:: quickstart-output.txt
   :language: text

Your file system should now look similar to this::

    crawler
    └── docs
        ├── index.rst
        ├── conf.py
        ├── Makefile
        └── make.bat
        ├── _build
        ├── _static
        ├── _templates

We have a top-level ``docs`` directory in the main project directory.
Inside of this is:

``index.rst``:
    This is the index file for the documentation, or what lives at ``/``.
    It normally contains a *Table of Contents* that will link to all other
    pages of the documentation.

``conf.py``: 
    Allows for customization of Sphinx.
    You won't need to use this too much yet,
    but it's good to be familiar with this file.

``Makefile`` & ``make.bat``: 
    This is the main interface for local development,
    and shouldn't be changed.

``_build``:  
    The directory that your output files go into.

``_static``: 
    The directory to include all your static files, like images.

``_templates``: 
    Allows you to override Sphinx templates to customze look and feel.

Building docs
-------------

Let's build our docs into HTML to see how it works.
Simply run::

    # Inside top-level docs/ directory.
    make html

This should run Sphinx in your shell, and output HTML.
At the end, it should say something about the documents being ready in
``_build/html``.
You can now open them in your browser by typing::

    open _build/html/index.html

You can also view it by running a web server in that directory::

    # Inside docs/_build/html directory.
    python -m SimpleHTTPServer

Then open your browser to http://localhost:8000.

This should display a rendered HTML page that says **Welcome to Crawler’s documentation!** at the top.

``make html`` is the main way you will build HTML documentation locally.
It is simply a wrapper around a more complex call to Sphinx,
which you can see as the first line of output.

Extra Credit
************

Have some extra time left?
Check out these other cool things you can do with Sphinx.

Understanding ``conf.py``
-------------------------

Sphinx is quite configurable,
which can be a bit overwhelming.
However, 
the ``conf.py`` file is quite well docuemnted.
You can read through it and get some ideas about what all it can do.

A couple of my favorite settings:

* html_theme

This is all well documented in the Sphinx :ref:`sphinx:build-config` doc.