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
    for i in range(50):
        L_crit_tracks = ct.crit_tracks(G)
        n_routes = 0
        final_length = 0
        # Create routes until there are no more critical tracks
        while len(L_crit_tracks) != 0:
            start = s2.start_select(G, L_crit_tracks, L_station)
            print(n_routes)
            route = rc.Route(start, [start], 0, 0, L_crit_tracks)
            optimal = route2object.route2object(G, max_length, route)
            final_length += optimal[2]
            print(optimal)
            L_crit_tracks = optimal[3]
            n_routes += 1
        print(n_routes)
        K = 10000 - (n_routes * 20 + (final_length / 10))
        print(K)
        if K > k_max:
            k_max = K
    print(k_max)
