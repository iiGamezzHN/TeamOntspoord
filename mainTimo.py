# Imports
import os
import sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd

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

import_dict = imp.open_stations('data', 'StationsHolland.csv')
import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)

stations = {}
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location, station_dict[x]['Neighbours'])


G = nw.Network_Graph(st.Station).graph

if __name__ == "__main__":
    L_crit_tracks = route2.crit_tracks(G)
    L_station = cs.create_starts(G, 7)
    crit_tracks_visited = []
    tot_weight = 0
    max_length = 120
    n_crit_tracks = 0
    i = 0
    final_length = 0
    while len(L_crit_tracks) != 0:
        print(i)
        station = L_station[i]
        L_route = [station]
        optimal = route2.route2(G, station, L_route, tot_weight, max_length, n_crit_tracks, L_crit_tracks)
        final_length += optimal[2]
        print(optimal)
        L_crit_tracks = optimal[3]
        i += 1
    i += 1
    K = 10000 - (i * 20 + (final_length / 10))
    print(K)
