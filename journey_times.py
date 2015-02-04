import pybingmaps as bing
from time import localtime
API_KEY = ''
JOURNEYS = {'Journey 1': ['37.423658,-122.090236', '37.423368,-122.075602'],
            'Journey 2': ['37.415563,-122.078091', '37.420471,-122.078048', '37.420769,-122.082919'],
            'Journey 3': ['37.415563,-122.078091', '37.416713,-122.082919', '37.420769,-122.082919'],
            'Journey 4': ['37.438053,-122.111737', '37.429926,-122.100440', '37.426211,-122.094442', '37.420769,-122.082919'],
            'Journey 5': ['37.438053,-122.111737', '37.422181,-122.091889', '37.420769,-122.082919'],
            'Journey 6': ['37.438053,-122.111737', '37.415563,-122.078091', '37.420471,-122.078048', '37.420769,-122.082919']}
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


