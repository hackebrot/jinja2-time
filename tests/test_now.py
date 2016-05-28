# -*- coding: utf-8 -*-

import pytest

from freezegun import freeze_time
from jinja2 import Environment, exceptions


@pytest.fixture
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
    template = environment.from_string(
        "{% now '" + valid_tz + "', '%Y-%m' %}"
    )

    assert template.render() == '2015-12'


def test_environment_datetime_format(environment):
    environment.datetime_format = '%a, %d %b %Y %H:%M:%S'

    template = environment.from_string("{% now 'utc' %}")

    assert template.render() == "Wed, 09 Dec 2015 23:33:01"


def test_delta_plus(environment):
    template = environment.from_string(
         "{% now 'utc' ='+86400' %}"
        )
    assert template.render() == "2015-12-10"


def test_delta_subs(environment):
    template = environment.from_string(
         "{% now 'utc' ='-86400' %}"
        )
    assert template.render() == "2015-12-08"


def test_delta_format(environment):

    template = environment.from_string(
         "{% now 'utc' ='-3661', '%a, %d %b %Y %H:%M:%S' %}"
        )
    assert template.render() == "Wed, 09 Dec 2015 22:32:00"
