import import_data as imp
import copy

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
Doesn't visit stations more than twice, does keep track of amount of critical
tracks visited, and removes critical tracks from list of critical tracks when
visited.

L_route: list of visited stations, in order
tot_weight: total length of route
L_crit_tracks: list of critical tracks
n_crit_tracks: number of critical visited
station: current station
neighbour: current neighbour
max_length: maximal length of route
opt = values of optimal route
"""


def route2object(network, max_length, route):
    # Find neighbours of given station, and see if they can be appended to
    # route. If so, continue finding their neighbours. Keep track of number of
    # critical tracks visited (n_crit_tracks). Variable is a copy to put
    # into next level.

    for neighbour in network[route.station]:
        route_copy = copy.deepcopy(route)
        weight = int(network[route_copy.station][neighbour]['weight'])
        route_copy.tot_weight = weight + route_copy.tot_weight
        # Make sure you don't go over total length, don't visit station more than twice
        if route_copy.tot_weight < max_length and route_copy.L_route.count(neighbour) < 2:
            for track in route_copy.L_crit_tracks:
                if route_copy.station in track and neighbour in track:
                    route_copy.n_crit_tracks += 1
                    # Create updated list of critical tracks, remove visited crit track
                    route_copy.L_crit_tracks.remove(track)
                    break
            route_copy.L_route.append(neighbour)
            route_copy.station = neighbour
            route2object(network, max_length, route_copy)

    # Create global variables for route with optimal amount of critical tracks
    # visited

    global n_crit_opt
    global L_route_opt
    global length_opt
    global L_crit_tracks_opt

    try:
        n_crit_opt
    except NameError:
        n_crit_opt = route.n_crit_tracks
        L_route_opt = route.L_route
        length_opt = route.tot_weight
        L_crit_tracks_opt = route.L_crit_tracks

    # Checks if current route is better than previous optimal route
    if route.n_crit_tracks > n_crit_opt:
        n_crit_opt = route.n_crit_tracks
        L_route_opt = route.L_route
        length_opt = route.tot_weight
        L_crit_tracks_opt = route.L_crit_tracks
    elif route.n_crit_tracks == n_crit_opt and route.tot_weight < length_opt:
        L_route_opt = route.L_route
        length_opt = route.tot_weight
        L_crit_tracks_opt = route.L_crit_tracks

    # If it reaches end of calculation returns optimal route values, reset
    # optimal values
    if len(route.L_route) == 1:
        n_crit_opt_copy = n_crit_opt
        L_route_opt_copy = L_route_opt.copy()
        length_opt_copy = length_opt
        n_crit_opt = 0
        L_route_opt = []
        length_opt = max_length
        return L_route_opt_copy, n_crit_opt_copy, length_opt_copy, L_crit_tracks_opt
