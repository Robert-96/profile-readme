API Documentation
=================

.. contents:: Table of Contents
    :local:
    :backlinks: none


Basic API Usage
---------------

This section gives you a brief introduction to the Python API for ``profile-readme``:

.. code-block:: python

    from profile_readme import get_github_context, ProfileGenerator


    context = {}
    filters = {}

    # If you don't need the GitHub data you can remove the next line
    context.update(**get_github_context('octocat'))


    ProfileGenerator.render(
        template_path="README-TEMPLATE.md",
        output_path="README.md",
        context=context,
        filters=filters
    )


To change behavior, pass the appropriate keyword arguments to ``ProfileGenerator.render``.

- To change which template to use, set ``template_path`` (default is ``README-TEMPLATE.md``).
- To change the output file, pass in ``output_path`` (default is ``README.md``).
- To supply data to your template, pass in ``context`` (default is ``None``).
- To add your own filters, simply set ``filters`` (default is ``None``).


.. Note:: By default the ``render`` command pasess the output of the ``get_github_context``
    to the template context.


API
---

This part of the documentation lists the full API reference of all public classes and functions.

.. module:: profile_readme


.. autoclass:: ProfileGenerator
   :inherited-members:


.. autofunction:: get_github_context
