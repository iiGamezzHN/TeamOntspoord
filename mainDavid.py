# Imports
import os
import sys

# de map waarin het project staat
located_map = "TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

# test
print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code")

# import bestanden vanuit de map code
import network as nw
import import_data as imp
import station_class as st
import calc_crit_tracks as ct

# import files using the functions from import_data.py
import_dict = imp.open_stations('data', 'StationsHolland.csv')
import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)

# adding the stations as instances of the class Station
stations = {}
list_stations = []
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location, station_dict[x]['Neighbours'])
    list_stations.append(x)

G = nw.Network_Graph(st.Station).graph

max_length = 120
k_max = 0
n_best = 3
depth = 2
list_crit_stations = ct.crit_tracks(G)
