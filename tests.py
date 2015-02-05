#!/usr/bin/env python

"""Unit tests for the `py-bing-maps.py` file."""

import unittest
try:
    from urlparse import urlparse, parse_qs
except ImportError:  # pragma: no cover
    # For older versions of Python.
    from urlparse import urlparse
    from cgi import parse_qs
from mock import Mock
from pybingmaps import pybingmaps
from pybingmaps import Bing


def set_up():
    """
    Mock both and json.loads' return value. Makes for fast unit tests.
    """
    pybingmaps.urlopen = Mock()
    route_dict = {'route': ['first_result', 'second_result'], 'total': 2}
    pybingmaps.json.loads = Mock(return_value=route_dict)
    pybingmaps.zlib.decompress = Mock()
    pybingmaps.API_KEY = 'my_api_key'


def call_args(kind='query'):
    """Find out what urlopen called while mocking."""
    call = pybingmaps.urlopen.call_args[0][0]
    parsed_call = urlparse(call)
    if kind == 'query':
        return  parse_qs(parsed_call.query)
    elif kind == 'path':
        return parsed_call.path


class BingClassInitTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_uninitialized_api_key(self):
        self.assertEqual(Bing().api_key, 'my_api_key')

    def test_initialized_api_key(self):
        self.assertEqual(Bing('called_api_key').api_key, 'called_api_key')

    def test_version_argument_with_float(self):
        self.assertEqual(Bing(version=2.5).version, '2.5')

    def test_version_argument_with_string(self):
        self.assertEqual(Bing(version='2.5').version, '2.5')


class RouteMethodTest(unittest.TestCase):

    def setUp(self):
        set_up()

    def test_nonempty_search_url_path(self):
        Bing().route('some route')
        path = call_args('path')
        self.assertEqual(path, '/REST/v1/Routes')

    def test_empty_search_url_keys(self):
        Bing().route('')
        route = call_args()
        self.assertEqual(route.keys(), ['apikey'])

    def test_nonempty_search_url_keys(self):
        Bing().route('some route')
        route = call_args()
        self.assertEqual(route.keys(), ['q', 'apikey'])

    def test_search_url_keys_with_page_arg(self):
        Bing().route('some route', page=2)
        route = call_args()
        self.assertEqual(route.keys(), ['q', 'apikey', 'page'])

    def test_search_url_keys_with_page_limit_arg(self):
        Bing().route('some route', page_limit=5)
        route = call_args()
        self.assertEqual(route.keys(), ['q', 'apikey', 'page_limit'])

    def test_search_url_keys_with_multiple_kwargs(self):
        Bing().route('some route', page=2, page_limit=5)
        route = call_args()
        self.assertEqual(route.keys(), ['q', 'apikey', 'page', 'page_limit'])

    def test_search_url_keys_for_lion_king(self):
        Bing().route('the lion king')
        route = call_args()
        assert 'my_api_key' in route['apikey']
        assert 'the lion king' in route['q']

    def test_search_url_keys_for_ronin(self):
        Bing().route('ronin')
        route = call_args()
        assert 'my_api_key' in route['apikey']
        assert 'ronin' in route['q']

    def test_search_results_for_standard_datatype(self):
        results = Bing().route('some route')
        self.assertEqual(results, ['first_result', 'second_result'])

    def test_search_results_for_movies_datatype(self):
        results = Bing().route('some route', 'movies')
        self.assertEqual(results, ['first_result', 'second_result'])

    def test_search_results_for_total_datatype(self):
        results = Bing().route('some route', 'total')
        self.assertEqual(results, 2)

if __name__ == '__main__':
    unittest.main()