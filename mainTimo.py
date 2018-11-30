# Imports
import os
import sys

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

import network as nw
import station_class as st
import import_data as imp
import parameter_class as pc
import calc_crit_tracks as ct
import route2_object_n_best as best
from hillclimber_for_route2 import route2_hill as hc


if __name__ == "__main__":
    # Gather relevant info
    stations = {}
    L_station = []
    import_dict = imp.open_stations('data', 'StationsHolland.csv')
    import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
    station_dict = imp.add_connections_dict(import_dict, import_list)
    for x in station_dict:
        location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
        stations[x] = st.Station(x, x, station_dict[x]['Critical'], location, station_dict[x]['Neighbours'])
        L_station.append(x)
    G = nw.Network_Graph(st.Station).graph

    max_length = 120
    k_max = 0
    n_best = 30
    L_crit_tracks = ct.crit_tracks(G)
    tot_crit_tracks = len(L_crit_tracks)
    parameters = pc.Parameters(G, max_length, tot_crit_tracks, L_station)
    solution_set = hc(parameters, n_best, L_crit_tracks)

    for object in solution_set[0]:
        print(object.L_route)
    print(solution_set[1])
