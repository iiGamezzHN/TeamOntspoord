import networkx as nx
import random
import csv
import matplotlib.pyplot as plt
import import_data as imp

#import trainNetwork

"""
Creates a random route with given network, starting point, and max_length. Tries
to find unvisited critical stations first, then unvisited in general, then
random. Returns list of visited stations (including starting point) and total
length
"""

def random_route(network, station, max_length):
    dict_stat = imp.open_stations('data','StationsHolland.csv')
    L_crit_stat = []
    L_tracks = []
    for item in dict_stat:
        if dict_stat[item]['Critical'] == 'Kritiek':
            L_crit_stat.append(item)

    tot_length = 0

    # List of stations in route
    L_route = [station]
    while True:

        # Get list of neighbours of station
        neighbors = network[station]
        L_n_all= []
        for n in neighbors:
            L_n_all.append(n)

        station_old = station
        L_n_unvisited = []
        L_n_crit_unv = []

        # Look for critical and unvisited stations
        for item in L_n_all:
            if item not in L_route:
                L_n_unvisited.append(item)
                if item in L_crit_stat:
                    L_n_crit_unv.append(item)

        # Go to random unvisited critical station, elif unvisited, else random
        if len(L_n_crit_unv) != 0:
            station=random.choice(L_n_crit_unv)
        elif len(L_n_unvisited) != 0:
            station=random.choice(L_n_unvisited)
        else:
            station=random.choice(L_n_all)

        weight = int(network[station][station_old]['weight'])

        # Make sure you don't go over max length, but try to find suitable station
        if tot_length + weight  > max_length:
            L_n2 = []
            for station_2 in L_n_all:
                weight_2 = int(network[station_2][station_old]['weight'])
                if weight_2 + tot_length < max_length:
                    L_n2.append(station_2)

            if len(L_n2) == 0:
                break
            else:
                station=random.choice(L_n2)
                weight = int(network[station][station_old]['weight'])

        L_tracks.append([station_old, station])
        tot_length += weight
        L_route.append(station)
    print(L_tracks)
    return L_route, tot_length
