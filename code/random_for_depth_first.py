from depth_first_n_best import depth_first_n_best as n_best_routes
import route_class as rc
from starts2 import start_select as s2
import random


def depth_random(para, n_best, L_crit_tracks, n_iterations):
    """
    This function chooses from the n_best routes a random route until no more
    critical tracks remain. It does this n_iterations times, saving the best
    result. Returns a list of route objects, the k-score of this set, and the
    progression of the k-score.
    """
    k_solution = 0
    k_evolution = []
    for j in range(0, n_iterations):
        print("Did " + str(j) + " iterations")
        k_score = 0
        set = []
        L_crit_tracks_route = L_crit_tracks.copy()
        i = 0
        # Pick random routes from routes_list until no more criticals
        while True:
            start = s2(para, L_crit_tracks_route)
            route = rc.Route(start, [start], 0, 0, L_crit_tracks_route, 0, 0)
            routes_list = n_best_routes(para, route, n_best)
            random_route = random.choice(routes_list)
            set.append(random_route[0])
            L_crit_tracks_route = random_route[0].L_crit_tracks
            # Choose best if at last route
            if len(L_crit_tracks_route) == 0:
                set[i] = routes_list[0][0]
                break
            i += 1
        # Check for best scores
        for object in set:
            k_score += object.k_score_ind
        if k_score > k_solution:
            k_solution = k_score
            solution_set = set.copy()
        k_evolution.append(k_solution)

    return solution_set, k_solution, k_evolution
