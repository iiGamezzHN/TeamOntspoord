def calc_route_score(nw, track_lists, list_crit_tracks, station_dict):
    track_pairs = []
    for track in track_lists:
        temp = []
        for station in range(len(track)-1):
            temp.append([track[station],track[station+1]])
        track_pairs.append(temp)
    print (track_pairs)

    crit_stations(station_dict)

def crit_stations(station_dict):
    crit_stations = []
    for x in station_dict:
        if station_dict[x]['Critical'] == 'Kritiek':
            print(x, station_dict[x]['Neighbours'])
            crit_stations.append(x)
    return crit_stations
