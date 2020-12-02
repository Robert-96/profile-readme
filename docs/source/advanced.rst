Advanced Usage
==============

This part of the documentation covers some of the library's
more advanced features and patterns.

.. contents:: Table of Contents
    :local:
    :backlinks: none


Using Custom Build Scripts
--------------------------

The command line shortcut is convenient, but sometimes your project
needs something different than the defaults. To change them, you can
write a custom build script.

A minimal build script looks something like this:

.. code-block:: python

    from profile_readme import get_github_context, ProfileGenerator


    context = {}

    # If you don't need the GitHub data you can remove the next line
    context.update(**get_github_context('octocat'))


    if __name__ == "__main__":
        ProfileGenerator.render(
            template_path="README-TEMPLATE.md",
            output_path="README.md",
            context=context
        )

Finally, just save the script as ``build.py`` (or something similar) and run it with your Python interpreter.

.. code-block:: console

    $ python build.py

.. Note:: Don't forgot to also update ``.github/workflows/readme.yml``.
   Replace ``python3 -m profile_readme render`` with ``python3 build.py``.


Loading Data
------------

The simplest way to supply data to the template is to pass ``ProfileGenerator.render`` a mapping from variable names to their values (a “context”) as the ``context`` keyword argument.

.. code-block:: python

    from profile_readme import get_github_context, ProfileGenerator


    context = {
        greeting='Hello, world!'
    }

    # If you don't need the GitHub data you can remove the next line
    context.update(**get_github_context('octocat'))


    if __name__ == "__main__":
        ProfileGenerator.render(
            template_path="README-TEMPLATE.md",
            output_path="README.md",
            context=context
        )

Anything added to this dictionary will be available in the template:

.. code-block::

    # Title

    {{ greeting }}

Filters
-------

Variables can be modified by `Filters`_. All the standard Jinja2 filters
are supported (you can found the full list `here`__).  To add your own
filters, simply pass filters as an argument to ``ProfileGenerator``.

.. code-block:: python

    from profile_readme import get_github_context, ProfileGenerator


    context = get_github_context('octocat')
    filters = {
        'hello': lambda x: 'Hello, {}!',
    }

    # If you don't need the GitHub data you can remove the next line
    context.update(**get_github_context('octocat'))


    if __name__ == "__main__":
        ProfileGenerator.render(
            template_path="README-TEMPLATE.md",
            output_path="README.md",
            context=context,
            filters=filters
        )

Then you can use them in your template as you would expect:

.. code-block::

    {{ 'World'|hello }}


.. _Filters: https://jinja.palletsprojects.com/en/2.11.x/templates/#filters
.. _Build in Filters: https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters

__ `Build in Filters`_
