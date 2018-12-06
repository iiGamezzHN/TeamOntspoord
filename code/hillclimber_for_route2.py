import route2_object_n_best as best
import route_class as rc
from starts2 import start_select as s2
import copy

"""
For all routes found with route2_object_n_best find the next best routes until
done. Select the route with the highest final k-score, then does the same thing
for the second route.
"""


def route2_hill(para, n_best, L_crit_tracks):
    i = 0
    while True:
        start = s2(para, L_crit_tracks)
        route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0)
        # Find set of n_best routes
        if i == 0:
            routes_list = best.route2_object_n_best(para, route, n_best)
        else:
            routes_list = next_routes_list_optimal
        # For every route in routes_list calculate the next route with highest
        # k-score
        try:
            solution_set
        except NameError:
            solution_set = []
            k_best = 0

        k_optimal = 0
        List_L_critical_tracks = []
        for item in routes_list:
            L_crit_tracks = item[0].L_crit_tracks.copy()
            k_total = 0
            j = 0
            if L_crit_tracks not in List_L_critical_tracks:
                List_L_critical_tracks.append(L_crit_tracks)
                while len(L_crit_tracks) != 0:
                    start = s2(para, L_crit_tracks)
                    route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0)
                    next = best.route2_object_n_best(para, route, n_best)
                    item.append(next[0][0])
                    L_crit_tracks = next[0][0].L_crit_tracks.copy()
                    if j == 0:
                        next_routes_list = next
                    j += 1
                for object in item:
                    k_total += object.k_score_ind
                if k_total > k_optimal:
                    k_optimal = k_total
                    set_optimal = copy.deepcopy(item)
                    k_current_route = item[0].k_score_ind
                    next_routes_list_optimal = next_routes_list



        # Add best route
        solution_set.append(set_optimal[0])
        route = set_optimal[0]
        L_crit_tracks = route.L_crit_tracks
        k_best += k_current_route
        i += 1
        print("Found route "+str(i))

        if len(route.L_crit_tracks) == 0:
            break

    return solution_set, k_best
