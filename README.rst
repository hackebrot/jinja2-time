===========
Jinja2 Time
===========

|travis-ci|

Jinja2 Extension for Dates and Times

.. |travis-ci| image:: https://travis-ci.org/hackebrot/jinja2-time.svg?branch=master
    :target: https://travis-ci.org/hackebrot/jinja2-time
    :alt: See Build Status on Travis CI

Installation
------------

**jinja2-time** is *not yet* available for download from `PyPI`_ via `pip`_.

For the time being please install via::

    $ pip install git+https://github.com/hackebrot/jinja2-time.git

It will automatically install `Jinja2`_ along with `arrow`_.

.. _`Jinja2`: https://github.com/mitsuhiko/jinja2
.. _`PyPI`: https://pypi.python.org/pypi
.. _`arrow`: https://github.com/crsmithdev/arrow
.. _`pip`: https://pypi.python.org/pypi/pip/

Usage
-----

The extension comes with a ``now`` tag that provides convenient access to the
`arrow.now() API`_ from your templates:

.. _`arrow.now() API`: http://crsmithdev.com/arrow/#arrow.factory.ArrowFactory.now


Code of Conduct
---------------

Everyone interacting in the jinja2-time project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, jinja2-time is free and open source software

.. _`MIT`: http://opensource.org/licenses/MIT
