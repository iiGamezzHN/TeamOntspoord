# import transform_tracklist as tt
import score as sc


def calc_route_score(nw, track_lists, station_dict):
    pair_stations(track_lists)
    crit_stations(station_dict)
    unique = sc.unique(station_dict)
    # transform = tt.transform(nw, track_lists)
    # print("begin")
    # for x in track_lists:
    #     print(x)
    # print("")
    Scores = []
    new_track_lists = []
    for x in track_lists:
        temp = sc.score(nw, [x], unique[0], unique[1])
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
    # for x in new_track_lists:
    #     if new_track_lists.count(x) >= 2:
    #         for y in range(new_track_lists.count(x)-1):
    #             new_track_lists.remove(x)
    #
    #     print(x)
    # for i in range(len(new_track_lists)):
    #     print(new_track_lists[i], Scores[i])
    # print("")
    for x in new_track_lists:
        if new_track_lists.count(x) >= 2:
            for y in range(new_track_lists.count(x)-1):
                ind = new_track_lists.index(x)
                del new_track_lists[ind]
                del Scores[ind]
    # for i in range(len(new_track_lists)):
    #     print(new_track_lists[i], Scores[i])
    # print(len(Scores), len(new_track_lists))
    # print("")
    return new_track_lists, Scores


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
