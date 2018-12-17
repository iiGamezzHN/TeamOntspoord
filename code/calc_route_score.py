import score as sc
from operator import itemgetter


def calc_route_score(nw, track_lists, station_dict, list_crit_tracks, n_best):
    if 'Utrecht Centraal' in station_dict:
        length = 180  # Max length for Nationaal
    else:
        length = 120  # Max length for Holland

    unique = sc.unique(station_dict)  # Returns critical tracks

    Scores = []
    new_track_lists = []

    for x in track_lists:
        # Score for individual route x
        temp = calc_score(nw, [x], unique[1], list_crit_tracks)

        if temp[4] > length:  # If minute length of route > max minutes
            new_x = x.copy()
            while True:  # Remove last track until minute length fits
                path = new_x[:-1]
                temp2 = calc_score(nw, [path], unique[1], list_crit_tracks)

                if temp2[4] <= length:
                    Scores.append(calc_score(nw, [path], unique[1],
                                             list_crit_tracks))
                    new_track_lists.append(path)
                    break

                new_x = path
        else:
            Scores.append(calc_score(nw, [x], unique[1], list_crit_tracks))
            new_track_lists.append(x)

    for x in new_track_lists:  # Remove duplicates
        if new_track_lists.count(x) >= 2:
            for y in range(new_track_lists.count(x)-1):
                ind = new_track_lists.index(x)
                del new_track_lists[ind]
                del Scores[ind]

    scores = []
    for x in new_track_lists:  # Make new list with route, score and time
        y = calc_score(nw, [x], unique[1], list_crit_tracks)
        scores.append([x, y[0], y[-1]])

    if n_best > len(scores):  # Set n_best to nr of routes
        n_best = len(scores)

    # Sort scores descending on the score
    best = sorted(scores, key=itemgetter(1), reverse=True)[0:n_best]

    return best  # Return sorted list of n_best scores


def calc_score(nw, track_lists, unique_ct, list_crit_tracks):
    tot_len_ct = len(unique_ct)  # Number of unique tracks
    tracks = pair_stations(track_lists)  # Get pairs between stations of track

    time = 0
    bkv = []  # Used critical tracks

    for pair in tracks:
        for crit in list_crit_tracks:
            if pair[0] in crit and pair[1] in crit:  # Check if pair is in crit list
                for ucrit in unique_ct:
                    if pair[0] in ucrit[0] and pair[1] in ucrit[0]:  # Get the weight
                        if pair not in bkv and pair[-1:]+pair[:-1] not in bkv:
                            bkv.append(pair)  # Add pair to used crit tracks
                            time += ucrit[1]
                        else:
                            time += ucrit[1]  # For second time crit track

        if pair not in list_crit_tracks and pair[-1:] + pair[:-1] not in list_crit_tracks:
            time += nw[pair[0]][pair[1]]['weight']  # For a not crit tracks

    p = len(bkv)/tot_len_ct
    S = p*10000 - (1*20 + time/10)

    return S, p, len(bkv), tot_len_ct, time


def pair_stations(track_lists):
    track_pairs = []

    for track in track_lists:
        temp = []

        for station in range(len(track)-1):
            # ['Alkmaar','Castricum','Hoorn'] to
            # [['Alkmaar','Castricum'],['Castricum','Hoorn']]
            temp.append([track[station], track[station+1]])

        track_pairs.extend(temp)

    return track_pairs
