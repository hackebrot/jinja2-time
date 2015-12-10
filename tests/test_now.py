# -*- coding: utf-8 -*-

import pytest

from freezegun import freeze_time
from jinja2 import Environment, exceptions


@pytest.fixture(scope='session')
def environment():
    return Environment(extensions=['jinja2_time.TimeExtension'])


@pytest.yield_fixture(autouse=True)
def freeze():
    freezer = freeze_time("2015-12-09 23:33:01")
    freezer.start()
    yield
    freezer.stop()


def test_tz_is_required(environment):
    with pytest.raises(exceptions.TemplateSyntaxError):
        environment.from_string('{% now %}')


def test_utc_default_datetime_format(environment):
    template = environment.from_string("{% now 'utc' %}")

    assert template.render() == "2015-12-09"


@pytest.fixture(params=['utc', 'local', 'Europe/Berlin'])
def valid_tz(request):
    return request.param


def test_accept_valid_timezones(environment, valid_tz):
    template = environment.from_string("{% now '" + valid_tz + "' %}")

    assert '2015' in template.render()
