import transform_tracklist as tt
import score as sc


def calc_route_score(nw, track_lists, station_dict):
    pair_stations(track_lists)
    crit_stations(station_dict)
    unique = sc.unique(station_dict)
    transform = tt.transform(nw, track_lists)
    Scores = []
    for x in track_lists:
        temp = sc.score(nw, [x], unique[0], unique[1])
        Scores.append(sc.score(nw, [x], unique[0], unique[1]))

    return track_lists, Scores


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
