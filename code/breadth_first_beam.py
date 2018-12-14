import calc_route_score as crs
import route_class as rc
from operator import itemgetter


def main(graph, list_routes, depth, station_dict, list_crit_tracks,
         max_length, n_best):
    time = True

    while time:
        a = bfb(graph, list_routes, depth)

        scores = crs.calc_route_score(graph, a, station_dict, list_crit_tracks)
        best = select_best_n(scores, n_best)

        if all(x[-1] >= 100 for x in best):
            time = False

        list_routes = []

        for x in best:
            list_routes.append(rc.Route(x[0][-1], x[0], x[2], 0,
                               list_crit_tracks, x[1]))
        # time += 1

    print("")
    print("")
    return list_routes


def select_best_n(scores, n_best):
    # time = 0
    routes = []

    for i in range(len(scores[0])):
        individual_route = scores[0][i]
        individual_score = scores[1][i][0]
        individual_time = scores[1][i][4]
        routes.append([individual_route, individual_score, individual_time])

    routes = sorted(routes, key=itemgetter(1), reverse=True)[0:n_best]
    # time = routes[0][2]
    return routes  # time


def bfb(graph, list_routes, depth):
    # keep track of all the paths to be checked
    # start = [[x[-1]] for x in start if x[-1] not in explored]
    start = []
    routes = []
    explored = []

    for x in list_routes:
        start.append([x.station])
        routes.append(x.L_route)
        explored.extend(x.L_route[:-1])

    queue = start
    # return path if start is goal
    depth_paths = []

    # keeps looping until all possible paths have been checked
    while queue:
        for x in queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]

            if node not in explored:
                neighbours = graph[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is goal
                    if len(new_path) == depth:
                        depth_paths.append(new_path)
                    elif len(new_path) > depth:
                        explore = list(set([y for x in depth_paths for y in x[:-1]]))
                        explored.extend(explore)
                        temp2 = update_tracks(routes, depth_paths)
                        for x in temp2:
                            if temp2.count(x) >= 2:
                                for y in range(temp2.count(x)-1):
                                    temp2.remove(x)
                        return temp2


def update_tracks(all_tracks, new_all_tracks):
    new_route = []
    for x in all_tracks:
        for y in new_all_tracks:
            if x[-1] == y[0]:
                new_route.append(x + y[1:])
    return new_route
