Blackbear: Standard Library Data and Math Tools
========================================
.. image:: https://github.com/cgdeboer/blackbear/actions/workflows/python-app.yml/badge.svg
    :target: https://app.travis-ci.com/cgdeboer/blackbear

.. image:: https://img.shields.io/pypi/v/blackbear.svg
    :target: https://pypi.org/project/blackbear/

Blackbear is an organic (standard library) library for key-based data manipulation and
math using only built-in python ``dicts`` and ``sets`` (without ``numpy, pandas, polars``).

**Justification**: there are a lot of great python-based data tools that make working
with relational data much easier. pandas_ is such a tool, and is well suited to working with
large(ish) datasets. numpy_ and polars_ are also great tools, though not as helpful if you rely
on relational/labeled data. Unfortunately, pandas_ can be excruciatingly slow when used repeatedly
on smaller data sets (see benchmarks). This can be the case in simulation tools, that have
"unvectorizable" step functions. ``blackbear`` can be used to replace some of the functionality
used in ``pandas.Series``, basic math on aligned index (``keys()``).

.. image:: https://raw.githubusercontent.com/cgdeboer/blackbear/master/docs/blackbear.jpeg
    :width: 400


Example Code:

.. code-block:: python

    >>> import blackbear as bb
    >>> data = {'foo': 60.0,
                'bar': 16.0,
                'baz': 24.0}
    >>> bb.add_scalar(data, 10)
    {'foo': 70.0,
     'bar': 26.0,
     'baz': 34.0}
    >>> blue = {'foo': 60.0,
                'bar': 16.0,
                'baz': 24.0}
    >>> green = {'foo': 40.0,
                 'bar': 4.0,
                 'baz': 6.0}
    >>> bb.add(blue, green)
    {'foo': 100.0,
     'bar': 20.0,
     'baz': 40.0}


Performance
---------------
"No numpy_, no pandas_, not even polars_, I bet this is really, really slow. Right ?"

For certain use cases, it can be faster than any of those. Here is a guide:

- Use ``blackbear`` for frequent (millions) operations on small collections (< 20 items) where matching on an index (i.e dict keys) is needed.
- Do not use ``blackbear`` for operations on larger collections (> 50000).

*See benchmark details and data below.*

.. _numpy: https://numpy.org/
.. _pandas: https://pandas.pydata.org/
.. _polars: https://www.pola.rs/


Feature Support
---------------

You are responsible for passing in the correct types to blackbear functions,
we didn't want the additional overhead of type checking.


Blackbear officially supports Python 3.8+.

Installation
------------

To install Blackbear, use `pipenv <http://pipenv.org/>`_ (or pip, of course):

.. code-block:: bash

    $ pipenv install blackbear

Documentation
-------------

Documentation beyond this readme will be available soon.


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request. Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/cgdeboer/blackbear
.. _AUTHORS: https://github.com/cgdeboer/blackbear/blob/master/AUTHORS.rst


Benchmarks
-----------------

> Performed on an Intel x64 chipped Mac (i7) with real blas and lapack installed.

**100000 X 5 Element-wise ops on collection of 10**

.. code-block::

    Pandas
    user 	0m35.212s
    Polars
    user	0m3.398s
    Numpy
    user	0m1.437s
    Blackbear
    user	0m0.601s

**1000000 X 5 Element-wise ops on collection of 10**

.. code-block::

    Pandas
    user	5m26.803s
    Polars
    user	0m24.115s
    Numpy
    user	0m6.734s
    Blackbear
    user	0m5.574s

**1000 X 5 Element-wise ops on collection of 10000**

.. code-block::

    Pandas
    user	0m1.406s
    Polars
    user	0m1.055s
    Numpy
    user	0m0.737s
    Blackbear
    user	0m2.703s

**1000 X 5 Element-wise ops on collection of 100000**

.. code-block::

    Pandas
    user	0m1.725s
    Polars
    user	0m1.230s
    Numpy
    user	0m1.035s
    Blackbear
    user	0m39.090s

**500000 X 5 Element-wise ops on collection of 5**

.. code-block::

    Pandas
    user	2m46.098s
    Polars
    user	0m12.899s
    Numpy
    user	0m3.674s
    Blackbear
    user	0m2.025s
