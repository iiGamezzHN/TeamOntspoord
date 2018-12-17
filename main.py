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
import mainDavid as md
from lookahead_for_depth_first import look_ahead as la
from random_for_depth_first import depth_random as dr
import breadth_first_search as bfs
import routes as rt
import traject_class as tc
import score as sc
import random_route as rr
import hillclimber_obj_orien as hh
import transform_tracklist as tt
import simulated_annealing as sa

# import files using the functions from import_data.py

if sys.argv[1] == "Holland":
    import_dict = imp.open_stations('data', 'StationsHolland.csv')
    import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
if sys.argv[1] == "Nationaal":
    import_dict = imp.open_stations('data', 'StationsNationaal.csv')
    import_list = imp.open_connections('data', 'ConnectiesNationaal.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)


# adding the stations as instances of the class Station
stations = {}
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                             station_dict[x]['Neighbours'])
# update certain labels
for x in stations:
    if 'Amsterdam' in stations[x].label:
        stations[x].update_single('Amsterdam', 'A.')
    if 'Rotterdam' in stations[x].label:
        stations[x].update_single('Rotterdam', 'R.')
    if 'Den Haag' in stations[x].label:
        stations[x].update_single('Den Haag', 'DH.')

# test an instance of the class Station
print(stations['Amsterdam Centraal'].information())


# Create the network
L = nw.Network_Graph(st.Station)
print(L.information())


apct = sc.unique(station_dict)[0]
uct = sc.unique(station_dict)[1]


def depth_first_look_ahead(region, all, n_best):
    L_station = []
    for x in station_dict:
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
    solution_string = '['

    # Print solutions, create graph
    for object in solution_set[0]:
        print(object.L_route)
        solution_string += (str(object.L_route) + '\n')
    print(solution_set[1])
    plt.plot(solution_set[2], 'o-')
    plt.xlabel('Amount of routes found (0 is the route without look-ahead)')
    plt.ylabel('K-score')
    plt.title('Evolution of K-score with depth first with look ahead')
    if all:
        with open("resultaten/depth_look_"+region+"_all.txt", "a") as myfile:
            myfile.write(solution_string)
            myfile.write(']\n')
            myfile.write(solution_set[1] + '\n')
        plt.savefig("resultaten/depth_look" + region + 'All')
    else:
        with open("resultaten/depth_look_"+region+"_notAll.txt", "a") as myfile:
            myfile.write(str(solution_string))
            myfile.write(']\n')
            myfile.write(str(solution_set[1]) + '\n')
        plt.savefig("resultaten/depth_look" + region + 'notAll')
    plt.show()


def depth_first_random(region, all, n_best, n_iterations):
    L_station = []
    for x in station_dict:
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
    solution_string = '['

    # Print solutions, create graph
    for object in solution_set[0]:
        print(object.L_route)
        solution_string += (str(object.L_route) + '\n')
    print(solution_set[1])
    plt.plot(solution_set[2], '-')
    plt.xlabel('Iterations')
    plt.ylabel('K-score')
    plt.title('Evolution of K-score with depth first with random choice')
    if all:
        plt.savefig("resultaten/depth_random" + region + 'All')
        with open("resultaten/depth_random_"+region+"_all.txt", "a") as myfile:
            myfile.write(str(solution_string))
            myfile.write(']\n')
            myfile.write(str(solution_set[1]) + '\n')
    else:
        plt.savefig("resultaten/depth_random" + region + 'notAll')
        with open("resultaten/depth_random_"+region+"_notAll.txt", "a") as myfile:
            myfile.write(str(solution_string))
            myfile.write(']\n')
            myfile.write(str(solution_set[1]) + '\n')
    plt.show()


def breadth_first_beam(region, all_crit, depth, n_best):
    md.breadth_first_beam_main(region, all_crit, depth, n_best)


if __name__ == "__main__":
    # Running depth first with random selection
    if sys.argv[2] == 'breadth_first_beam':
        if len(sys.argv) == 3:
            breadth_first_beam(sys.argv[1], False, 5, 10)
        else:
            try:
                depth_first_random(sys.argv[1], sys.argv[3], int(sys.argv[4]),
                                   int(sys.argv[5]))
            except:
                print("Invalid Input: usage: python main.py region"
                      "breadth_first_beam")

    if sys.argv[2] == 'depth_first_random':
        if len(sys.argv) == 3:
            depth_first_random(sys.argv[1], False, 30, 50)
        else:
            try:
                depth_first_random(sys.argv[1], sys.argv[3], int(sys.argv[4]),
                                   int(sys.argv[5]))
            except:
                print("Invalid Input: usage: python main.py region"
                      "depth_first_random all_critical n_best iterations")

    # Running depth first with look ahead
    if sys.argv[2] == 'depth_first_look_ahead':
        if len(sys.argv) == 3:
            depth_first_look_ahead(sys.argv[1], False, 20)
        else:
            try:
                depth_first_look_ahead(sys.argv[1], sys.argv[3],
                                       int(sys.argv[4]))
            except:
                print("Invalid Input: usage: python main.py"
                      " region depth_first_look_ahead all_critical n_best")

    # Draw the variable 'tracks', the edges are green if they are vistited once
    # and the are red when they are vistied multiple times
    if sys.argv[2] == 'draw_routes':
        tracks = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'],['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Gouda'],['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Laan v NOI'],['Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss', 'Nijmegen', 'Arnhem Centraal'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle'],['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal', 'Dordrecht', 'Rotterdam Blaak', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Gouda', 'Den Haag Centraal'],['Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum']]

        print(sc.score(L.graph, tracks, apct, uct)[0])
        # L.draw_choice(['track',tt.transform(L.graph,endtest)[0],uct],egdes_option=False)
        L.draw_choice(['all tracks', tt.transform(L.graph, tracks)[0], uct],
                      egdes_option=False)

    # Create the beginning of tracks for 'draw_hillclimber' and 'draw_simulated'
    # to complete the tracks
    tracks = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk'],
    ['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert'],
    ['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Deventer', 'Zutphen'],
    ['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem'],
    ['Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum'],
    ['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle'],
    ['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal'],
    ['Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal']]
    W = tc.Trajects(L.graph, tracks)

    if sys.argv[2] == 'draw_hillclimber':
        new_track = hh.hillclimber(L, W, 8, 1000, -3, 180, apct, uct)[0].tracks
        print(new_track)
        print(sc.score(L.graph, new_track, apct, uct)[0])
        L.draw_choice(['all tracks', tt.transform(L.graph, new_track)[0], uct],
                      egdes_option=False)

    if sys.argv[2] == 'draw_simulated':
        new_track = sa.simulated_annealing(L, W, 8, 100, -3, 180,apct, uct).tracks
        print(new_track)
        print(sc.score(L.graph, new_track, apct, uct)[0])
        L.draw_choice(['all tracks', tt.transform(L.graph, new_track)[0], uct],
                      egdes_option=False)
