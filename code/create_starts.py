import networkx as nx
import import_data as imp
import random


"""
Creates a list of starting points for a given amount of routes. Starting points
are determined by finding neigbours of critical stations, and seeing which
ones have the fewest connections. Returns a list with starting locations.
"""


def create_starts(network, n_routes):

    # Create list of critical stations
    dict_stat = imp.open_stations('data', 'StationsHolland.csv')
    L_crit_stat = []
    for item in dict_stat:
        if dict_stat[item]['Critical'] == 'Kritiek':
            L_crit_stat.append(item)

    start_list = []

    # Search for starting points

    for i in range(0, n_routes):
        station = L_crit_stat[i]
        neighbours = network[station]
        L_n = []
        L_n_fewest = []
        i = 0
        # Look for neighbouring stations of criticals, exclude criticals
        # themselves and choose one with fewest connections
        for item in neighbours:
            if item not in L_crit_stat:
                L_n.append(item)
                L_n_neighbours = network[item]
                if i == 0:
                    length_shortest = len(L_n_neighbours)
                    L_n_fewest.append(item)
                else:
                    if len(L_n_neighbours) < length_shortest:
                        L_n_fewest = [item]
                        length_shortest = len(L_n_neighbours)
                    elif len(L_n_neighbours) == length_shortest:
                        L_n_fewest.append(item)

            i += 1

        if len(L_n_fewest) != 0:
            start_list.append(random.choice(L_n_fewest))
        else:
            start_list.append(random.choice(L_n))

    return start_list
