def test(nw, start, nb, used, depth):
    if depth > 0:
        depth = depth - 1
        for x in start:
            for y in nw[x]:
                if y not in used:
                    nb.append(y)
        for x in start:
            used.append(x)
        start = set(start)
        nb = set(nb)
        print(start, nb)
        test(nw, nb, [], used, depth)


def bfb(graph, start, depth):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    depth_paths = []

    # keeps looping until all possible paths have been checked
    while queue:
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
                    # print(sum([len(x)/depth for x in depth_paths if
                    # len(x) == depth]))
                    return depth_paths

            # mark node as explored
            explored.append(node)
