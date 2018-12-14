# import transform_tracklist as tt
import score as sc


def calc_route_score(nw, track_lists, station_dict, list_crit_tracks):
    # pair_stations(track_lists)
    # crit_stations(station_dict)
    unique = sc.unique(station_dict)

    Scores = []
    new_track_lists = []
    for x in track_lists:
        temp = sc.score(nw, [x], unique[0], unique[1])
        # print(list_crit_tracks)
        calc_score(nw, [x], unique[1], list_crit_tracks)
        if temp[4] > 120:
            new_x = x.copy()
            while True:
                path = new_x[:-1]
                temp2 = sc.score(nw, [path], unique[0], unique[1])

                if temp2[4] <= 120:
                    Scores.append(sc.score(nw, [path], unique[0], unique[1]))
                    new_track_lists.append(path)
                    break

                new_x = path
        else:
            Scores.append(sc.score(nw, [x], unique[0], unique[1]))
            new_track_lists.append(x)

    for x in new_track_lists:
        if new_track_lists.count(x) >= 2:
            for y in range(new_track_lists.count(x)-1):
                ind = new_track_lists.index(x)
                del new_track_lists[ind]
                del Scores[ind]

    return new_track_lists, Scores

def calc_score(nw, track_lists, unique_ct, list_crit_tracks):
    tot_len_ct = len(unique_ct)
    tracks = pair_stations(track_lists)  # Get pairs between stations of track
    tracks = [item for sublist in tracks for item in sublist]
    bkv =[]
    time = 0
    # print(tracks)
    # print(list_crit_tracks)
    # print("")
    print(tracks)
    for pair in tracks:
        for crit in list_crit_tracks:
            if pair[0] in crit and pair[1] in crit:  # Check if pair is in crit list
                for ucrit in unique_ct:
                    if pair[0] in ucrit[0] and pair[1] in ucrit[0]:  # Get the weight
                        if pair not in bkv and pair[-1:]+pair[:-1] not in bkv:
                            bkv.append(pair)
                            time += ucrit[1]
                        else:
                            time += ucrit[1]
    print(bkv)
    print(time)
    p = len(bkv)/tot_len_ct
    S = p*10000 - (1*20 + time/10)
    print(S)
    print("")
    return S, p, len(bkv), tot_len_ct, time


def crit_stations(station_dict):
    crit_stations = []

    for x in station_dict:
        if station_dict[x]['Critical'] == 'Kritiek':
            crit_stations.append(x)

    return crit_stations


def pair_stations(track_lists):
    track_pairs = []

    for track in track_lists:
        temp = []

        for station in range(len(track)-1):
            temp.append([track[station], track[station+1]])

        track_pairs.append(temp)

    return track_pairs
