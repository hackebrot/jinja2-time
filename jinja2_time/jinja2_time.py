# -*- coding: utf-8 -*-

import arrow

from jinja2 import nodes, environmentfilter
from jinja2.ext import Extension


class TimeExtension(Extension):
    tags = set(['now'])

    def __init__(self, environment):
        super(TimeExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            date_format='%Y-%m-%d',
        )

    def _now(self, timezone, date_format):
        date_format = date_format or self.environment.date_format
        return arrow.now(timezone).strftime(date_format)

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        args = [parser.parse_expression()]

        if parser.stream.skip_if('comma'):
            args.append(parser.parse_expression())
        else:
            args.append(nodes.Const(None))

        call = self.call_method('_now', args, lineno=lineno)

        return nodes.Output([call], lineno=lineno)


@environmentfilter
def year(environment, value, timezone='utc', date_format=None):
    date_format = date_format or environment.date_format
    date = arrow.Arrow.strptime(value, date_format, tzinfo=timezone)
    return date.strftime('%Y')
