import calc_route_score as crs

def main(graph, start, depth, explored, station_dict, max_length):
    time = 0;
    routes = []
    # while time < 120:
    all_tracks = bfb(graph, start, depth, explored)
    scores = crs.calc_route_score(graph, all_tracks[0], station_dict)
    start = all_tracks[0]
    explored = all_tracks[1]

    for i in range(len(scores[0])):
        individual_route = scores[0][i]
        individual_score = scores[1][i][0]
        individual_time = scores[1][i][4]
        if individual_time > time:
            time = individual_time
        routes.append([individual_route, individual_score, individual_time])
    new_all_tracks = bfb(graph, start, depth, explored)
    print(update_tracks(all_tracks[0], new_all_tracks[0]))

    return # print(routes, time)


def update_tracks(all_tracks, new_all_tracks):
    new_route = []
    for x in all_tracks:
        for y in new_all_tracks:
            if x[-1] == y[0]:
                new_route.append(x + y[1:])
    return new_route


def bfb(graph, start, depth, explored):
    # keep track of all the paths to be checked
    start = [[x[-1]] for x in start if x[-1] not in explored]
    queue = start
    # return path if start is goal
    depth_paths = []
    temp = []

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
                        temp = list(set([y for x in depth_paths for y in x[:-1]]))
                        explored.extend(temp)
                        # print(sum([len(x)/depth for x in depth_paths if
                        # len(x) == depth]))
                        return depth_paths, explored
