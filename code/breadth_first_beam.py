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

def bfb(network, parameters, start, route, depth, used):
    while depth > 0:
        used.append(start)
        neighbours = []
        for x in network[start]:
            if x not in used:
                neighbours.append(x)

        print("Used")
        print(used)
        print("Neighbours")
        print(neighbours)

        for x in neighbours:
            return bfb(network, parameters, neighbours[0], route, depth, used)

        depth = depth - 1

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    nr = 0
    # keep looping until there are nodes still to be checked
    while queue:

        print(queue)
        # pop shallowest node (first node) from queue
        # node = queue.pop(0)
        for x in queue:
            if x not in explored:
                # add node to list of checked nodes
                explored.append(x)
                neighbours = graph[x]

                # add neighbours of node to queue
                for neighbour in neighbours:
                    if neighbour not in explored:
                        queue.append(neighbour)
        nr += 1
        print(nr)
    return explored
