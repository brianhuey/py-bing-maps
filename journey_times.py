import pybingmaps as bing
from time import localtime
import json
from datetime import datetime
from pytz import timezone
import pytz

API_KEY = open('api_key.txt', 'r').readline()
JOURNEYS = json.load(open('journeys.json','r'))
TRAVEL_TIMES = {}
bingmap = bing.Bing(API_KEY)
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

date_format='%m%d-%H%M'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific'))
current_time = 'data/' + str(date.strftime(date_format)) + '.txt'
write_file = open(current_time,'w')
write_file.write(json.dumps(TRAVEL_TIMES))
write_file.close()

