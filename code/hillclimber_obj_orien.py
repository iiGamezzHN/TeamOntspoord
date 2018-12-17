import traject_class as tc

def hillclimber(graph, traject, nr_tracks, iterations, cut_x, minutes, apct, uct):
    highscore = 0
    total_i = 0
    score_i_list = []
    for a in range(nr_tracks):
        print(a, 'len of track:', len(traject.tracks[a]))
        for b in range(iterations):
            total_i += 1
            new = traject.transform_track_return_if_impr(a, cut_x, minutes, apct, uct)
            if new != None:
                new_tracks = new[0]
                new_score = new[1]
                score_i_list.append([total_i,new_score])
                if new_score > highscore:
                    Y = tc.Trajects(graph.graph, new_tracks)
                    highscore = new_score
                    print(a,b,new_score,highscore, new_tracks[a])
        # if 'Y' in locals():
                    traject = Y
    return traject, score_i_list
