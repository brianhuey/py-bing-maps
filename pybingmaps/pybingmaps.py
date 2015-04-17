#!/usr/bin/env python

"""
Bing Maps API:  http://www.bingmapsportal.com
Main file for interacting with the Bing Maps API.
"""

from urllib import urlencode
import zlib
import os

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen


API_KEY = os.environ.get('BING_KEY')


class Bing(object):
    """
    An easy-to-use Python wrapper for the Bing Maps API.
    """

    def __init__(self, api_key='', version=1):
        if not api_key:
            self.api_key = API_KEY
        else:
            self.api_key = api_key
        assert self.api_key is not None, "No API Key"

        if isinstance(version, float):
            version = str(version)  # Eliminate any weird float behavior.
        self.version = version
        BASE_URL = 'http://dev.virtualearth.net/REST/v%s/' % version
        self.BASE_URL = BASE_URL
        self.routes_url = BASE_URL + 'Routes'
        self.traffic_url = BASE_URL + 'Traffic/Incidents/'

    def _load_json_from_url(self, url):
        """
        A wrapper around the api call. The response might be gzipped,
        which this will abstract away. Returns a JSON-decoded dictionary.
        """
        response = urlopen(url).read()

        # the response might be gzip'd
        try:
        # explanation of magic number:
        # http://stackoverflow.com/a/2695466/474683
            response = zlib.decompress(response, 16+zlib.MAX_WBITS)
        except zlib.error:
        # if there's an error, it's probably not gzip'd
            pass
        return json.loads(response)
    def route(self, journeys, **kwargs):
        """
        Bing Maps Route search. Returns a list of dictionaries.
        Journey dictionary required: {'wayPoint.1': ['lat,lng'], 'wayPoint.2': ['lat,lng']}
        Possible kwargs include: `wayPoint.2+n', 'heading', 'optimize'
        'avoid', 'distanceBeforeFirstTurn', 'heading', 'optimize', 'routeAttributes', 'routePathOutput', 'maxSolutions', 'tolerances', 'distanceUnit', 'dateTime', 'timeType', 'mfaxSolutions', 'travelMode'
        See https://msdn.microsoft.com/en-us/library/ff701717.aspx for descriptions.
        """
        search_url = [self.routes_url, '?']
        kwargs.update(journeys)
        kwargs.update({'key': self.api_key})
        search_url.append(urlencode(kwargs))
        data = self._load_json_from_url(''.join(search_url))
        return data
    def traffic(self, mapArea, **kwargs):
        """
        Bing Maps Traffic Incident search. Returns a list of dictionaries.
        mapArea string required: 'southLat, westLng, northLat, eastLng'
        Possible kwargs include: 'congestion', 'description', 'detour', 'start', 'end', 'incidentId', 'lane', 'lastModified', 'roadClosed', 'severity', 'toPoint', 'locationCodes', 'type', 'verified'
        See https://msdn.microsoft.com/en-us/library/hh441730.aspx for descriptions
        """
        search_url = [self.traffic_url, mapArea, '?']
        kwargs.update({'key': self.api_key})
        search_url.append(urlencode(kwargs))
        data = self._load_json_from_url(''.join(search_url))
        return data
