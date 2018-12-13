# Imports
import os
import sys

# de map waarin het project staat
located_map = "TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")
sys.path.append(parent_dir_name+"\\"+located_map+"\\code\\class")

# import bestanden vanuit de map code
import network as nw
import import_data as imp
import station_class as st
import calc_crit_tracks as ct
from starts2 import start_select as s2
import parameter_class as pc
import route_class as rc
import breadth_first_beam as bfb
import calc_route_score as crs

# import files using the functions from import_data.py
import_dict = imp.open_stations('data', 'StationsHolland.csv')
import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)

# adding the stations as instances of the class Station
stations = {}
list_stations = []
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                             station_dict[x]['Neighbours'])
    list_stations.append(x)


G = nw.Network_Graph(st.Station).graph

max_length = 120
depth = 3
n_best = 10
list_crit_tracks = ct.crit_tracks(G, "Holland", False)
tot_crit_tracks = len(list_crit_tracks)
parameters = pc.Parameters(G, max_length, tot_crit_tracks, list_stations)

start = s2(parameters, list_crit_tracks)
route = rc.Route(start, [start], 0, 0, list_crit_tracks, 0)
explored = []

final_routes = bfb.main(G, [route], depth, station_dict, list_crit_tracks,
                        max_length, n_best)
sorting = []
for x in final_routes:
    sorting.append(x.k_score_ind)
sorting = sorted(sorting, reverse=True)

final_track = []
for x in final_routes:
    if x.k_score_ind == sorting[0]:
        station = x.station
        L_route = x.L_route
        tot_weight = x.tot_weight
        n_crit_tracks = x.n_crit_tracks
        L_crit_tracks = x.L_crit_tracks
        k_score_ind = x.k_score_ind
        final_track.append(rc.Route(station, L_route, tot_weight,
                           n_crit_tracks, L_crit_tracks, k_score_ind))

a = crs.pair_stations([final_track[0].L_route])[0]
for x in a:
    for y in list_crit_tracks:
        if x[0] in y and x[1] in y:
            list_crit_tracks.remove(y)

final_track[0].L_crit_tracks = list_crit_tracks

for x in final_track:
    print(x.station)
    print(x.L_route)
    print(x.tot_weight)
    print(x.L_crit_tracks)
    print(x.k_score_ind)
# for i in range(len(scores[0])):
#     individual_route = scores[0][i]
#     score = scores[1][i][0]
#     time = scores[1][i][4]
#     print(individual_route, score, time)
