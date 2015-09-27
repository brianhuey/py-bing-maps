# py-bing-maps
Bing Maps wrapper for Python

A python wrapper for the Bing Maps REST API.

You need a Microsoft account and an API key to use.

Use
--------
``` python
import py-bing-maps

bing = py-bing-maps.bing('insert api key as string')
```
Return route JSON

``` python
start = (37.828947, -122.249114)
end = (37.824608, -122.256431)
bing.route(start, end)
```

Get travel time and travel distance
``` python
bing.travelTime(start, end)
bing.travelDistance(start, end)
```