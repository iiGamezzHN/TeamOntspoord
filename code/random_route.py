import networkx as nx
import random

# Creates random route with given starting point and length
def random_route(start, max_length):
    station = start
    tot_length = 0

    # List of stations in route
    L_route = [station]
    while True:

        # Get list of neighbours of station
        neighbors = G[station]
        L_n= []
        for n in neighbors:
            L_n.append(n)

        # Choose random neighbour and get length
        station_old = station
        station=random.choice(L_n)
        weight = int(G[station][station_old]['weight'])

        # Make sure you don't go over max length (There still might be another station within max length)
        if tot_length + weight  > max_length:
            break

        tot_length += weight
        L_route.append(station)
    print(L_route)
    print(tot_length)
