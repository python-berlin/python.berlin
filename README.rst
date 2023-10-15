=============
python.berlin
=============

The `python.berlin <https://python.berlin>`_ website allows all Berlin Python
User Groups to introduce themselves, present slides, code examples etc.

🤝 Collaboration
================

.. collaboration:

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/python-berlin/python.berlin_website/fork>`_
of our `GitHub Repository
<https://github.com/python-berlin/python.berlin_website>`_ and make your changes
there.

Download and installation
-------------------------

#. Download

   .. code-block:: console

    $ git clone git@github.com:python-berlin/python.berlin.git

#. Create virtual environment

   .. code-block:: console

    $ cd python.berlin
    $ $ python3 -m venv .
    $ . bin/activate
    $ python -m pip install --upgrade pip
    $ python -m pip install -r requirements_dev.txt
    $ pre-commit install

#. Create HTML

   .. code-block:: console

    $ cd docs
    $ make html
