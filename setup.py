#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='jinja2-time',
    version='0.2.0',
    author='Raphael Pierzina',
    author_email='raphael@hackebrot.de',
    maintainer='Raphael Pierzina',
    maintainer_email='raphael@hackebrot.de',
    license='MIT',
    url='https://github.com/hackebrot/jinja2-time',
    description='Jinja2 Extension for Dates and Times',
    long_description=read('README.rst'),
    packages=[
        'jinja2_time',
    ],
    package_dir={'jinja2_time': 'jinja2_time'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
        'arrow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
    keywords=['jinja2', 'extension', 'time'],
)
