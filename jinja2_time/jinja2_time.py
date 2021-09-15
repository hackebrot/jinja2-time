# -*- coding: utf-8 -*-

import re
from datetime import datetime

from dateutil import tz
from dateutil.relativedelta import relativedelta

from jinja2 import nodes
from jinja2.ext import Extension


class TimeExtension(Extension):
    tags = set(['now'])

    def __init__(self, environment):
        super(TimeExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(datetime_format='%Y-%m-%d')

    def _datetime(self, timezone, operator, offset, datetime_format):
        tzi = _gettz(timezone)
        d = datetime.now(tzi)

        # Parse replace kwargs from offset and include operator
        rd_params = {}
        for param in offset.split(','):
            interval, value = param.split('=')
            rd_params[interval.strip()] = float(value.strip())

        rd = relativedelta(**rd_params)

        if operator == '-':
            d -= rd
        elif operator == '+':
            d += rd
        else:
            raise ValueError('Unknown operator: %s' % operator)

        if datetime_format is None:
            datetime_format = self.environment.datetime_format
        return d.strftime(datetime_format)

    def _now(self, timezone, datetime_format):
        if datetime_format is None:
            datetime_format = self.environment.datetime_format

        tzi = _gettz(timezone)
        return datetime.now(tzi).strftime(datetime_format)


    def parse(self, parser):
        lineno = next(parser.stream).lineno

        node = parser.parse_expression()

        if parser.stream.skip_if('comma'):
            datetime_format = parser.parse_expression()
        else:
            datetime_format = nodes.Const(None)

        if isinstance(node, nodes.Add):
            call_method = self.call_method(
                '_datetime',
                [node.left, nodes.Const('+'), node.right, datetime_format],
                lineno=lineno,
            )
        elif isinstance(node, nodes.Sub):
            call_method = self.call_method(
                '_datetime',
                [node.left, nodes.Const('-'), node.right, datetime_format],
                lineno=lineno,
            )
        else:
            call_method = self.call_method(
                '_now',
                [node, datetime_format],
                lineno=lineno,
            )
        return nodes.Output([call_method], lineno=lineno)


_TZOFFSET_MATCH = re.compile('(?P<sgn>[+-])?(?P<hh>\d{2}):?(?P<mm>\d{2})?^')


def _parse_isotz(tzstr):
    m = _TZOFFSET_MATCH.match(tzstr)
    if m:
        sign = -1 if m.group('sgn') == '-' else 1

        hh = int(m.group('hh'))
        mm_g = mm.group('mm')
        mm = int(mm_g) if mm_g else 0

        total_seconds = sign * (hh * 3600 + (mm * 60))
        return tz.tzoffset(None, total_seconds)

    return None


def _gettz(tzstr):
    """ Parse a time zone string into a time zone """

    tzstr_l = tzstr.lower()
    if not tzstr or tzstr_l == 'utc':
        return tz.tzutc()

    if tzstr_l == 'local':
        return tz.tzlocal()

    tzi = tz.gettz(tzstr)

    if tzi is None:
        tzi = _parse_isotz(tzstr)

    if tzi is None:
        raise TzParseError('Unknown time zone %s' % tzstr)

    return tzi


class TzParseError(ValueError):
    pass
