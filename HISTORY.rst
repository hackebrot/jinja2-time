.. :changelog:

History
-------

0.3.0 (????-??-??)
------------------

* Limit arrow version to 0.13.2 when install on python >3.0 and <=3.4


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
