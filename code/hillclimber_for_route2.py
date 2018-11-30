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
        routes_list = best.route2_object_n_best(para, route, n_best)
        # For every route in routes_list calculate the next route with highest
        # k-score
        for item in routes_list:
            L_crit_tracks = item[0].L_crit_tracks.copy()
            while len(L_crit_tracks) != 0:
                start = s2(para, L_crit_tracks)
                route = rc.Route(start, [start], 0, 0, L_crit_tracks, 0)
                next = best.route2_object_n_best(para, route, 1)
                item.append(next[0][0])
                L_crit_tracks = next[0][0].L_crit_tracks.copy()

        k_optimal = 0

        try:
            solution_set
        except NameError:
            solution_set = []
            k_best = 0

        # Calculate the total score of all routes together per set
        for set in routes_list:
            k_total = 0
            for object in set:
                k_total += object.k_score_ind
            if k_total > k_optimal:
                k_optimal = k_total
                set_optimal = copy.deepcopy(set)
                k_current_route = set[0].k_score_ind

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
