import networkx as nx
import random_route.py as rand
import import_data as imp


"""
Creates a list of starting points for a given amount of routes. Starting points
are determined by finding neigbours of critical stations
"""


def create_starts(network, n_routes):

    # Create list of critical stations
    dict_stat = imp.open_stations('data','StationsHolland.csv')
    L_crit_stat = []
    for item in dict_stat:
        if item['Critical'] == 'Kritiek':
            L_crit_stat.append(item)

    start_list = []

    # Search for starting points, still needs to be improved
    for i in range(0, n_routes):
        station = L_crit_stat[i]
        neighbours = network[station]
        for item in neighbours:
            L_n.append(item)
        start_list.append(random.choice(L_n))

    return start_list
