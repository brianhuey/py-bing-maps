#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import py-bing-maps

setup(name="py-bing-maps",
      version="1.0",
      description="Bing Maps Python API",
      long_description='',
      keywords="bing maps python traveltime python traffic",
      author="S. Brian Huey",
      author_email="sbhuey@gmail.com",
      url="https://github.com/brianhuey/py-bing-aps",
      license="Unlicense (a.k.a. Public Domain)",
      packages=["py-bing-maps"],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                  ],
      test_suite="test.py",
      tests_require=["mock", "Mock"])