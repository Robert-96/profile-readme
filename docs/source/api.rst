API Documentation
=================

This part of the documentation lists the full API reference of all public classes and functions.

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


API
---

.. module:: profile_readme


.. autoclass:: ProfileGenerator
   :inherited-members:


.. autofunction:: get_github_context
