
def transform_last(network, solution_set, para):
    n_routes = len(solution_set[0])
    last_route = solution_set[0][n_routes - 1]
    n_tracks_last = len(last_route.L_route)
    for i in range(0, n_tracks_last - 2):
        track = [last_route.L_route[i], last_route.L_route[i + 1]]
        track_length = network[track[0]][track[1]]['weight']
        change = False
        for route in solution_set[0][:-1]:
            route_length = len(route.L_route)
            if track[0] in route.L_route or track[1] in route.L_route:
                if route.L_route[0] == track[0] and route.tot_weight + track_length < para.max_length:
                    route.L_route.insert(0, track[1])
                    change = True
                    last_route.L_route.remove(track[1])
                    break
                elif route.L_route[0] == track[1] and route.tot_weight + track_length < para.max_length:
                    route.L_route.insert(0, track[0])
                    change = True
                    break
                elif route.L_route[route_length - 1] == track[0] and route.tot_weight + track_length < para.max_length:
                    route.L_route.append(track[1])
                    change = True
                    break
                elif route.L_route[route_length - 1] == track[1] and route.tot_weight + track_length < para.max_length:
                    route.L_route.append(track[0])
                    change = True
                    break
                else:
                    try:
                        index = route.L_route.index(track[0])
                        if route.tot_weight + 2 * track_length < para.max_length:
                            route.L_route.insert(index + 1, track[1])
                            route.L_route.insert(index + 2, track[0])
                            change = True
                            break
                    except ValueError:
                        index = route.L_route.index(track[1])
                        if route.tot_weight + 2 * track_length < para.max_length:
                            route.L_route.insert(index + 1, track[0])
                            route.L_route.insert(index + 2, track[1])
                            change = True
                            break
        if not change:
            break
    return solution_set
