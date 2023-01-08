=============
python.berlin
=============

The `python.berlin <https://python.berlin>`_ website allows all Berlin Python
User Groups to introduce themselves, present slides, code examples etc.

.. collaboration:

🤝 Collaboration
================

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/python-berlin/python.berlin_website/fork>`_
of our `GitHub Repository
<https://github.com/python-berlin/python.berlin_website>`_ and make your changes
there.

Download and installation
-------------------------

#. Download

   .. code-block:: console

    $ git clone git@github.com:python-berlin/python.berlin_website.git

#. Create virtual environment

   .. code-block:: console

    $ cd python.berlin_website
    $ python3 -m pip install -r requirements_dev.txt
    $ source bin/activate
    $ pre-commit install

#. Create HTML

   .. code-block:: console

    $ make html
