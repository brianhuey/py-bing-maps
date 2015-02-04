import pybingmaps as bing
from time import localtime
import json

API_KEY = open('api_key.txt', 'r').readline()
JOURNEYS = json.load(open('journeys.json','r'))
TRAVEL_TIMES = {}
bingmap = bing.Bing(API_KEY)
current_time = str(localtime().tm_mon) + '-' + str(localtime().tm_mday) + '-' + str(localtime().tm_hour) + '-' + str(localtime().tm_min)
for key in JOURNEYS:
    waypoints = len(JOURNEYS[key])
    waypoints_dic = {}
    waypoints_dic['wayPoint.1'] = JOURNEYS[key][0]
    waypoint_end_name = 'wayPoint.' + str(waypoints)
    waypoints_dic[waypoint_end_name] = JOURNEYS[key][-1]
    if waypoints > 2:
        count = 2
        for i in JOURNEYS[key][1:-1]:
            name = 'viaWaypoint.' + str(count)
            waypoints_dic[name] = i
            count += 1
    TRAVEL_TIMES[key] = bingmap.route(waypoints_dic)


