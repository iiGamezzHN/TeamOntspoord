# Imports
import os
import sys
import matplotlib.pyplot as plt

# de map waarin het project staat
located_map = "TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")
sys.path.append(parent_dir_name+"\\"+located_map+"\\code\\class")

import network as nw
import station_class as st
import import_data as imp
import parameter_class as pc
import calc_crit_tracks as ct
from lookahead_for_depth_first import look_ahead as la
from random_for_depth_first import depth_random as dr


def depth_first_look_ahead(region, all, n_best):
    stations = {}
    L_station = []
    import_dict = imp.open_stations('data', 'Stations' + region + '.csv')
    import_list = imp.open_connections('data', 'Connecties' + region + '.csv')
    station_dict = imp.add_connections_dict(import_dict, import_list)
    for x in station_dict:
        location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
        stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                                 station_dict[x]['Neighbours'])
        L_station.append(x)
    G = nw.Network_Graph(st.Station).graph

    # Get correct parameters
    if region == 'Holland':
        max_length = 120
    elif region == 'Nationaal':
        max_length = 180
    L_crit_tracks = ct.crit_tracks(G, region, all)
    tot_crit_tracks = len(L_crit_tracks)
    parameters = pc.Parameters(G, max_length, tot_crit_tracks, L_station)
    solution_set = la(parameters, n_best, L_crit_tracks)

    # Print solutions, create graph
    for object in solution_set[0]:
        print(object.L_route)
    print(solution_set[1])
    plt.plot(solution_set[2], 'o-')
    plt.xlabel('Amount of routes found (0 is the route without look-ahead)')
    plt.ylabel('K-score')
    plt.title('Evolution of K-score with depth first with look ahead')
    plt.show()


def depth_first_random(region, all, n_best, n_iterations):
    stations = {}
    L_station = []
    import_dict = imp.open_stations('data', 'Stations' + region + '.csv')
    import_list = imp.open_connections('data', 'Connecties' + region + '.csv')
    station_dict = imp.add_connections_dict(import_dict, import_list)
    for x in station_dict:
        location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
        stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                                 station_dict[x]['Neighbours'])
        L_station.append(x)
    G = nw.Network_Graph(st.Station).graph

    # Get correct parameters
    if region == 'Holland':
        max_length = 120
    elif region == 'Nationaal':
        max_length = 180
    L_crit_tracks = ct.crit_tracks(G, region, all)
    tot_crit_tracks = len(L_crit_tracks)
    parameters = pc.Parameters(G, max_length, tot_crit_tracks, L_station)
    solution_set = dr(parameters, n_best, L_crit_tracks, n_iterations)

    # Print solutions, create graph
    for object in solution_set[0]:
        print(object.L_route)
        print(object.tot_weight)
    print(solution_set[1])
    plt.plot(solution_set[2], '-')
    plt.xlabel('Iterations')
    plt.ylabel('K-score')
    plt.title('Evolution of K-score with depth first with random choice')
    plt.show()


if __name__ == "__main__":
    # Running depth first with random selection
    if sys.argv[1] == 'depth_first_random':
        if len(sys.argv) == 2:
            depth_first_random('Holland', False, 30, 1000)
        else:
            try:
                depth_first_random(sys.argv[2], sys.argv[3], int(sys.argv[4]),
                                   int(sys.argv[5]))
            except:
                print("Invalid Input: usage: python main.py depth_first_random"
                      "region all_critical n_best iterations")

    # Running depth first with look ahead
    if sys.argv[1] == 'depth_first_look_ahead':
        if len(sys.argv) == 2:
            depth_first_look_ahead('Holland', False, 50)
        else:
            try:
                depth_first_look_ahead(sys.argv[2], sys.argv[3],
                                       int(sys.argv[4]))
            except:
                print("Invalid Input: usage: python main.py"
                      "depth_first_look_ahead region all_critical n_best")
