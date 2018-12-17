from depth_first_n_best import depth_first_n_best as n_best_routes
import route_class as rc
from starts2 import start_select as s2
import copy


def look_ahead(para, n_best, L_crit_tracks):
    """
    For all routes found with route2_object_n_best find the next best routes
    until done. Select the route with the highest final k-score, then does the
    same thing for the second route and so on.
    Setting n-best to 1 will yield the same results as the original depth-first
    algorithm, albeit a bit slower.
    """
    i = 0
    # Define global best solutions, in case a solution that's found early is
    # best.
    global global_best_set
    global global_best_k
    global_best_k = 0
    while True:
        # Initialise routes
        start = s2(para, L_crit_tracks)
        route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0, 0)
        # Find set of n_best routes if first route
        if i == 0:
            start = 'Heerenveen'
            route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0, 0)
            routes_list = n_best_routes(para, route, n_best)
            solution_set = []
            k_solution = 0
            k_evolution = [0]
        # Use previously found set of routes
        else:
            routes_list = next_routes_list_optimal

        # For every route in routes_list calculate the next route with highest
        # k-score
        k_optimal = 0
        List_L_critical_tracks = []
        for item in routes_list:
            L_crit_tracks = item[0].L_crit_tracks.copy()
            k_total = 0
            j = 0
            # Don't continue with routes that are too similar to previous ones,
            # namely routes that have the same critical routes remaining
            if L_crit_tracks not in List_L_critical_tracks:
                List_L_critical_tracks.append(L_crit_tracks)
                # Calculate complete set of routes
                while len(L_crit_tracks) != 0:
                    start = s2(para, L_crit_tracks)
                    route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0, 0)
                    next = n_best_routes(para, route, n_best)
                    item.append(next[0][0])
                    L_crit_tracks = next[0][0].L_crit_tracks.copy()
                    # Keep set of routes for next route, to prevent double work
                    if j == 0:
                        next_routes_list = next
                    j += 1
                # Find best scores
                for object in item:
                    k_total += object.k_score_ind
                if k_total > k_optimal:
                    k_optimal = k_total
                    set_optimal = copy.deepcopy(item)
                    k_current_route = item[0].k_score_ind
                    next_routes_list_optimal = next_routes_list
        # Find first value for k_evolution
        if i == 0:
            for object in routes_list[0]:
                k_evolution[0] += object.k_score_ind

        # Add best route, if better than global best
        if k_optimal + k_solution > global_best_k:
            global_best_set = solution_set + set_optimal
            solution_set.append(set_optimal[0])
            route = set_optimal[0]
            global_best_k = k_optimal + k_solution
            k_evolution.append(k_optimal + k_solution)
            k_solution += k_current_route
        # Go back to gloabal best solution
        else:
            solution_set.append(global_best_set[i])
            route = global_best_set[i]
            k_evolution.append(global_best_k)
            k_solution += route.k_score_ind
        L_crit_tracks = route.L_crit_tracks

        i += 1
        print("Found route " + str(i))

        if len(route.L_crit_tracks) == 0:
            break

    return solution_set, k_solution, k_evolution
