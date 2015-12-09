# -*- coding: utf-8 -*-

import pytest

from jinja2 import Environment


@pytest.fixture(scope='session')
def environment():
    return Environment(extensions=['jinja2_time.TimeExtension'])


def test_foobar(environment):
    assert environment
