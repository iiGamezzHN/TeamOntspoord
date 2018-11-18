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

L_route: list of visited stations, in order
tot_weight: total length of route
L_crit_tracks: list of critical tracks
n_crit_tracks: number of critical visited
station: current station
neighbour: current neighbour
max_length: maximal length of route
child: copy to give as argument to function
"""


def route2(network, station, L_route, tot_weight, max_length, n_crit_tracks, L_crit_tracks):
    # Find neighbours of given station, and see if they can be appended to
    # route. If so, continue finding their neighbours. Keep track of number of
    # critical tracks visited (n_crit_tracks). Variable_child is a copy to put
    # into next level.
    for neighbour in network[station]:
        L_crit_tracks_child = L_crit_tracks.copy()
        n_crit_tracks_child = n_crit_tracks
        weight = int(network[station][neighbour]['weight'])
        tot_weight_child = weight + tot_weight
        # Make sure you don't go over total length, don't visit station more than twice
        if tot_weight_child < max_length and L_route.count(neighbour) < 2:
            for track in L_crit_tracks:
                if station in track and neighbour in track:
                    n_crit_tracks_child += 1
                    # Create updated list of critical tracks, remove visited crit track
                    L_crit_tracks_child = L_crit_tracks.copy()
                    L_crit_tracks_child.remove(track)
                    break
            L_route_child = L_route.copy()
            L_route_child.append(neighbour)
            route2(network, neighbour, L_route_child, tot_weight_child, max_length, n_crit_tracks_child, L_crit_tracks_child)

    # Create global variables for route with optimal amount of critical tracks
    # visited
    global n_crit_opt
    global L_route_opt
    global length_opt

    try:
        n_crit_opt
    except NameError:
        n_crit_opt = n_crit_tracks
        L_route_opt = L_route
        length_opt = tot_weight

    # Checks if current route is better than previous optimal route
    if n_crit_tracks > n_crit_opt:
        n_crit_opt = n_crit_tracks
        L_route_opt = L_route
        length_opt = tot_weight
    elif n_crit_tracks == n_crit_opt:
        if tot_weight < length_opt:
            L_route_opt = L_route
            length_opt = tot_weight

    # If it reaches end of calculation returns optimal route values
    if len(L_route) == 1:
        return L_route_opt, n_crit_opt, length_opt
