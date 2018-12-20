import calc_route_score as crs
import route_class as rc
from operator import itemgetter


def main(graph, list_routes, depth, station_dict, list_crit_tracks,
         max_length, n_best):
    if 'Utrecht Centraal' in station_dict:
        min = 160  # Minimun length of routes in Nationaal
    else:
        min = 100  # Minimum length of routes in Holland

    while True:
        a = bfb(graph, list_routes, depth)  # Returns list of routes from start

        if a is not None:  # To prevent NoneType error
            # Returns sorted scores for n_best routes
            scores = crs.calc_route_score(graph, a, station_dict,
                                          list_crit_tracks, n_best)

            testing1 = [x.L_route for x in list_routes]
            list_routes = []

            for x in scores:
                list_routes.append(rc.Route(x[0][-1], x[0], x[2], 0,
                                   list_crit_tracks, x[1], 0))

            testing2 = [x.L_route for x in list_routes]

            if testing1 == testing2:  # If begin and end are equal, stop
                break

            if all(x[-1] >= min for x in scores):
                break  # If all routes have minimun length, stop
        else:
            break

    return list_routes


def select_best_n(scores, n_best):
    if n_best > len(scores):  # If nr of routes is lower than n_best
        n_best = len(scores)  # Set n_best to nr of routes

    # Sort scores descending on the score
    best = sorted(scores, key=itemgetter(1), reverse=True)[0:n_best]

    return best


def bfb(graph, list_routes, depth):
    # keep track of all the paths to be checked
    start = []
    routes = []
    explored = []

    for x in list_routes:
        start.append([x.station])  # Makes a list with all starting points
        routes.append(x.L_route)  # Makes a list with all the current routes
        explored.extend(x.L_route[:-1])  # Makes a list of explored stations

    # print(start)
    # print('---------')

    queue = start
    depth_paths = []

    # keeps looping until all possible paths have been checked
    while queue:
        for x in queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]

            if explored.count(node) <= 1:
                neighbours = graph[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if len(new_path) == depth:  # Return path if depth reached
                        depth_paths.append(new_path)
                    #
                    elif len(new_path) > depth:
                        explore = list(set([y for x in depth_paths for y in
                                       x[:-1]]))
                        explored.extend(explore)
                        # Put old and new path together
                        temp2 = update_tracks(routes, depth_paths)
                        for x in temp2:  # Remove duplicate routes
                            if temp2.count(x) >= 2:
                                for y in range(temp2.count(x)-1):
                                    temp2.remove(x)
                        return temp2  # Return new complete path


def update_tracks(all_tracks, new_all_tracks):
    new_route = []
    for x in all_tracks:
        for y in new_all_tracks:
            # If last in old equals first in new, put together
            if x[-1] == y[0]:
                new_route.append(x + y[1:])
    return new_route
