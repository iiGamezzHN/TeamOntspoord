# Imports
import os
import sys

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

import random_route as rand
import create_starts as cs
import network as nw
import station_class as st
import import_data as imp
import route2
import route2object
import route_class as rc
import calc_crit_tracks as ct
import starts2 as s2
import route2_object_n_best as best

import_dict = imp.open_stations('data', 'StationsHolland.csv')
import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)

stations = {}
L_station = []
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location, station_dict[x]['Neighbours'])
    L_station.append(x)



G = nw.Network_Graph(st.Station).graph

if __name__ == "__main__":
    # Gather relevant info
    max_length = 120
    k_max = 0
    n_best = 10
    L_crit_tracks = ct.crit_tracks(G)
    tot_crit_tracks = len(L_crit_tracks)
    start = "Den Helder"
    route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0)

    best_routes = best.route2_object_n_best(G, max_length, route, tot_crit_tracks, n_best)
    print(best_routes)
    for item in best_routes:
        print(item[0].k_score_ind)
        print(item[0].L_route)
