CLI Documentation
=================

.. contents:: Table of Contents
    :local:
    :backlinks: none


Invocation
----------

.. code-block:: console

    $ profile-readme [...]


You can also invoke the command through the Python interpreter from the
command line:

.. code-block:: console

    $ python3 -m profile_readme [...]


Getting Help
------------

.. code-block:: console

    $ profile-readme --version    # show the profile-readme version
    $ profile-readme -h | --help  # show help message on command line


CLI
---

.. click:: profile_readme.cli:cli
  :prog: profile-readme
  :nested: full
