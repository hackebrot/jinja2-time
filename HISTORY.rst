.. :changelog:

History
-------

0.2.0 (2016-06-08)
------------------

Features:

* Relative time offset via ``"{% now 'utc' + 'hours=2,seconds=30' %}"`` or
  ``-`` to modify the rendered datetime


0.1.0 (2015-12-11)
------------------

First release on PyPI.

Features:

* TimeExtension with a ``now`` tag to get the current time in `jinja2`_
  templates

.. _`jinja2`: https://github.com/mitsuhiko/jinja2
