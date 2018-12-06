def bfb(graph, start, depth, explored):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    start = [x for x in start if x not in explored]
    print(start)
    queue = start
    # return path if start is goal
    depth_paths = []

    # keeps looping until all possible paths have been checked
    while queue:
        print(queue)
        # pop the first path from the queue
        path = queue.pop(0)
        path2 = queue.pop(0)
        print(path)
        # get the last node from the path
        node = path[-1]
        node2 = path2[-1]
        print(node)

        if node not in explored:
            neighbours = graph[node]
            print(neighbours)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                print(new_path)
                new_path.append(neighbour)
                print(new_path)
                queue.append(new_path)
                print(queue)
                print("")
                # return path if neighbour is goal
                if len(new_path) == depth:
                    depth_paths.append(new_path)
                    print(depth_paths)
                elif len(new_path) > depth:
                    # print(sum([len(x)/depth for x in depth_paths if
                    # len(x) == depth]))
                    print("")
                    print("final: ")
                    print(depth_paths)
                    print(explored)
                    return depth_paths

        if node2 not in explored:
            neighbours = graph[node2]
            print(neighbours)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path2)
                print(new_path)
                new_path.append(neighbour)
                print(new_path)
                queue.append(new_path)
                print(queue)
                print("")
                # return path if neighbour is goal
                if len(new_path) == depth:
                    depth_paths.append(new_path)
                    print(depth_paths)
                elif len(new_path) > depth:
                    # print(sum([len(x)/depth for x in depth_paths if
                    # len(x) == depth]))
                    print("")
                    print("final 2: ")
                    print(depth_paths)
                    print(explored)
                    return depth_paths

            # mark node as explored
            explored.append(node)


# def test(nw, start, nb, used, depth):
#     if depth > 0:
#         depth = depth - 1
#         for x in start:
#             for y in nw[x]:
#                 if y not in used:
#                     nb.append(y)
#         for x in start:
#             used.append(x)
#         start = set(start)
#         nb = set(nb)
#         # print(start, nb)
#         test(nw, nb, [], used, depth)
