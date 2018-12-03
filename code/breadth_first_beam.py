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

def bfb(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
    # return path if start is goal
    val = []

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print('queue ', queue)
        print('node ', node)
        if node not in explored:
            neighbours = graph[node]
            print('nb ', neighbours)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)

                print("new_path ", new_path)
                queue.append(new_path)
                print('new_queue ', queue)
                # return path if neighbour is goal
                if len(new_path) == 4:
                    val.append(new_path)
                elif len(new_path) > 6:
                    print("")
                    print("")
                    print("Limit reached!")
                    print(sum([len(x)/4 for x in val if len(x) == 4]))
                    return

            # mark node as explored
            explored.append(node)
            print('ex ', explored)
            print("")

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        print(queue)
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)
