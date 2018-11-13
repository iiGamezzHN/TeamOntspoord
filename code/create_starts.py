import networkx as nx
import import_data as imp
import random


"""
Creates a list of starting points for a given amount of routes. Starting points
are determined by finding neigbours of critical stations
"""


def create_starts(network, n_routes):

    # Create list of critical stations
    dict_stat = imp.open_stations('data', 'StationsHolland.csv')
    L_crit_stat = []
    for item in dict_stat:
        if dict_stat[item]['Critical'] == 'Kritiek':
            L_crit_stat.append(item)
    start_list = []

    # Search for starting points, prefer stations with 1 connection to critical,
    # doesn't choose critical stations

    for i in range(0, n_routes):
        station = L_crit_stat[i]
        neighbours = network[station]
        L_n = []
        L_n_fewest = []
        i = 0
        for item in neighbours:
            if item not in L_crit_stat:
                L_n.append(item)
                x = network[item]
                if i == 0:
                    length_shortest = len(x)
                    L_n_fewest.append(item)
                else:
                    if len(x) < length_shortest:
                        L_n_fewest = [item]
                        length_shortest = len(x)
                    elif len(x) == length_shortest:
                        L_n_fewest.append(item)

            i += 1
        print(L_n_fewest)
        if len(L_n_fewest) != 0:
            start_list.append(random.choice(L_n_fewest))
        else:
            start_list.append(random.choice(L_n))

    return start_list
