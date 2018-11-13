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

    # Search for starting points, still needs to be improved

    for i in range(0, n_routes):
        station = L_crit_stat[i]
        neighbours = network[station]
        L_n = []
        for item in neighbours:
            L_n.append(item)
        start_list.append(random.choice(L_n))

    return start_list
