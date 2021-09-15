===========
Jinja2 Time
===========

|pypi| |pyversions| |license| |travis-ci|

Jinja2 Extension for Dates and Times

.. |pypi| image:: https://img.shields.io/pypi/v/jinja2-time.svg
   :target: https://pypi.python.org/pypi/jinja2-time
   :alt: PyPI Package

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/jinja2-time.svg
   :target: https://pypi.python.org/pypi/jinja2-time/
   :alt: PyPI Python Versions

.. |license| image:: https://img.shields.io/pypi/l/jinja2-time.svg
   :target: https://pypi.python.org/pypi/jinja2-time
   :alt: PyPI Package License

.. |travis-ci| image:: https://travis-ci.org/hackebrot/jinja2-time.svg?branch=master
    :target: https://travis-ci.org/hackebrot/jinja2-time
    :alt: See Build Status on Travis CI

Installation
------------

**jinja2-time** is available for download from `PyPI`_ via `pip`_::

    $ pip install jinja2-time

It will automatically install `jinja2`_ and its dependencies.

.. _`jinja2`: https://github.com/mitsuhiko/jinja2
.. _`PyPI`: https://pypi.python.org/pypi
.. _`pip`: https://pypi.python.org/pypi/pip/

Usage
-----

Now Tag
~~~~~~~

The extension comes with a ``now`` tag that retrieves the current datetime
in a given time zone from your templates. Time zone specifiers supported are:

- ``utc``
- ``local``
- ``[±]HH[:][MM]``
- Formats supported by `dateutil.tz.gettz`_ (IANA zones, GNU tz strings, etc)

You can control the output by specifying a format, that will be passed to
Python's `strftime()`_:

.. _`strftime()`: https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior
.. _`dateutil.tz.gettz`: https://dateutil.readthedocs.io/en/latest/tz.html#dateutil.tz.gettz

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_time.TimeExtension'])

    # Timezone 'local', default format -> "2015-12-10"
    template = env.from_string("{% now 'local' %}")

    # Timezone 'utc', explicit format -> "Thu, 10 Dec 2015 15:49:01"
    template = env.from_string("{% now 'utc', '%a, %d %b %Y %H:%M:%S' %}")

    # Timezone 'Europe/Berlin', explicit format -> "CET +0100"
    template = env.from_string("{% now 'Europe/Berlin', '%Z %z' %}")

    # Timezone 'utc', explicit format -> "2015"
    template = env.from_string("{% now 'utc', '%Y' %}")

    template.render()

Default Datetime Format
~~~~~~~~~~~~~~~~~~~~~~~

**TimeExtension** extends the environment with a ``datetime_format`` attribute.

It is used as a fallback if you omit the format for ``now``.

.. code-block:: python

    from jinja2 import Environment

    env = Environment(extensions=['jinja2_time.TimeExtension'])

    env.datetime_format = '%a, %d %b %Y %H:%M:%S'

    # Timezone 'utc', default format -> "Thu, 10 Dec 2015 15:49:01"
    template = env.from_string("{% now 'utc' %}")

    template.render()

Time Offset
~~~~~~~~~~~

**jinja2-time** implements a convenient interface to modify ``now`` by a
relative time offset:

.. code-block:: python

    # Examples for now "2015-12-09 23:33:01"

    # "Thu, 10 Dec 2015 01:33:31"
    "{% now 'utc' + 'hours=2, seconds=30' %}"

    # "Wed, 09 Dec 2015 23:22:01"
    "{% now 'utc' - 'minutes=11' %}"

    # "07 Dec 2015 23:00:00"
    "{% now 'utc' - 'days=2, minutes=33, seconds=1', '%d %b %Y %H:%M:%S' %}"

Further documentation on the underlying functionality can be found in the
`dateutil relativedelta docs`_.

.. _`dateutil relativedelta docs`: https://dateutil.readthedocs.io/en/latest/relativedelta.html#module-dateutil.relativedelta


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`file an issue`: https://github.com/hackebrot/jinja2-time/issues


Code of Conduct
---------------

Everyone interacting in the jinja2-time project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, jinja2-time is free and open source software

.. image:: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
   :align: left
   :alt: OSI certified
   :target: https://opensource.org/

.. _`MIT`: http://opensource.org/licenses/MIT
