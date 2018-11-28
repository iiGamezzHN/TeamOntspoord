import copy
from heapq import heappush, heappushpop, nlargest

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


def route2_object_n_best(network, max_length, route, tot_crit_tracks, n_best):
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
            route2_object_n_best(network, max_length, route_copy, tot_crit_tracks, n_best)

    route.k_score_ind = route.n_crit_tracks / tot_crit_tracks * 10000 - (20 + route.tot_weight / 10)

    global heap
    try:
        heap
    except NameError:
        heap = []

    if len(heap) < n_best:
        heappush(heap, route)
    else:
        heappushpop(heap, route)

    if len(route.L_route) == 1:
        heap = sorted(heap, reverse=True)
        routes_list = []
        for item in heap:
            routes_list.append([item])
        return routes_list
