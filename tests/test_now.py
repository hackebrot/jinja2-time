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


def test_add_time(environment):
    environment.datetime_format = '%a, %d %b %Y %H:%M:%S'

    template = environment.from_string(
        "{% now 'utc' + 'hours=2,seconds=30' %}"
    )

    assert template.render() == "Thu, 10 Dec 2015 01:33:31"


def test_substract_time(environment):
    environment.datetime_format = '%a, %d %b %Y %H:%M:%S'

    template = environment.from_string(
        "{% now 'utc' - 'minutes=11' %}"
    )

    assert template.render() == "Wed, 09 Dec 2015 23:22:01"


def test_offset_with_format(environment):
    environment.datetime_format = '%d %b %Y %H:%M:%S'

    template = environment.from_string(
        "{% now 'utc' - 'days=2, minutes=33,seconds=1', '%d %b %Y %H:%M:%S' %}"
    )

    assert template.render() == "07 Dec 2015 23:00:00"
