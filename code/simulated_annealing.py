from math import exp
from random import random

import traject_class as tc

def acceptance_probability(old_score, new_score, T):
    score_dif = (new_score-old_score)
    tt = (9400-old_score)/100
    a = exp(score_dif/20)
    return a


def simulated_annealing(graph, traject, nr_tracks, iterations, cut_x, minutes,apct, uct):
    for a in range(nr_tracks):
        print(a, 'len of track: ', len(traject.tracks[a]))
        old_score = traject.score(apct, uct)
        T = 1.0
        T_min = 0.1
        alpha = 0.8
        while T > T_min:
            i = 1
            while i <= iterations:
                new_sol = traject.transform_track(a, cut_x, minutes, apct, uct)
                new_score = new_sol[1]
                ap = acceptance_probability(old_score, new_score, T)
                r = random()
                if ap > r:
                    sol = new_sol
                    print(i, round(ap,2), round(r,2), new_score, new_score-old_score)
                    old_score = new_score
                    # traject = tc.Trajects(graph.graph, sol[0])

                i += 1
            print(a,T)
            T = T*0.8
        if 'sol' in locals():
            traject = tc.Trajects(graph.graph, sol[0])
            print(traject.information())
    return traject
