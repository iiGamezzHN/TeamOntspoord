import import_data as imp

"""
Returns a list of tuples, where elements are stations of a critical track
"""


def crit_tracks(network):
    dict_stat = imp.open_stations('data', 'StationsHolland.csv')
    L_crit_stat = []
    L_crit_tracks = []
    # List of critical stations
    for item in dict_stat:
        if dict_stat[item]['Critical'] == 'Kritiek':
            L_crit_stat.append(item)
    # Adds critical tracks as tuples to list. Makes sure there are no doubles
    for x in L_crit_stat:
        for neighbour in network[x]:
            double = False
            for item in L_crit_tracks:
                if x in item and neighbour in item:
                    double = True
                    break
            if not double:
                L_crit_tracks.append([x, neighbour])
    return(L_crit_tracks)


"""
Calculates all posible routes starting from a given station, with max length.
Doesn't visit stations twice, does keep track of amount of critical tracks
visited.
"""


def route2(network, station, L_route, tot_weight, max_length, n_k, crit):
    for item in network[station]:
        weight = int(network[station][item]['weight'])
        tot_weight_child = weight + tot_weight
        n_k_child = n_k
        if tot_weight_child > max_length or item in L_route:
            print(L_route)
            print(n_k)
            print(tot_weight)
        else:
            for track in crit:
                if item in track and station in track:
                    n_k_child += 1
            L_route_child = L_route.copy()
            L_route_child.append(item)
            route2(network, item, L_route_child, tot_weight_child, max_length, n_k_child, crit)
