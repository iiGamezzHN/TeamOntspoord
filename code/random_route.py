import networkx as nx
import random
import csv
import matplotlib.pyplot as plt
import functiesDavid
import trainNetwork

# Creates random route in a given network with given starting point, length


def random_route(network, station, max_length):
    tot_length = 0

    # List of stations in route
    L_route = [station]
    while True:

        # Get list of neighbours of station
        neighbors = network[station]
        L_n= []
        for n in neighbors:
            L_n.append(n)

        # Choose random neighbour and get length
        station_old = station
        L_crit = []

        # Look for critical stations that not have been visited yet
        for x in L_n:
            if x in stations_critical and x not in L_route:
                L_crit.append(x)

        # Go to random unvisited critical station if possible
        if len(L_crit) != 0:
            station=random.choice(L_crit)
        else:
            station=random.choice(L_n)

        weight = int(network[station][station_old]['weight'])

        # Make sure you don't go over max length, but try to find suitable station
        if tot_length + weight  > max_length:
            L_n2 = []
            for station_2 in L_n:
                weight_2 = int(network[station_2][station_old]['weight'])
                if weight_2 + tot_length < max_length:
                    L_n2.append(station_2)

            if len(L_n2) == 0:
                break
            else:
                station=random.choice(L_n2)
                weight = int(network[station][station_old]['weight'])

        tot_length += weight
        L_route.append(station)

    print(L_route)
    print(tot_length)


random_route(G, 'Amsterdam Centraal', 120)
