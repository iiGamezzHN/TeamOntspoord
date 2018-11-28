import route2_object_n_best as best
import route_class as rc
from starts2 import start_select as s2


def route2_hill(network, routes_list, max_length, tot_crit_tracks, stations):
    for item in routes_list:
        L_crit_tracks = item[0].L_crit_tracks
        start = s2(network, L_crit_tracks, stations)
        route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0)
        item.append(best.route2_object_n_best(network, max_length, route, tot_crit_tracks, 1))
