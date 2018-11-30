import random


def start_select(para, L_crit_tracks):
    min_station = []
    for station in para.stations_list:
        n_crit_tracks = sum(track.count(station) for track in L_crit_tracks)
        if len(min_station) == 0:
            min_station = [station]
            min = n_crit_tracks
            n_neighbours = len(para.network[station])
        elif n_crit_tracks < min and n_crit_tracks > 0:
            min = n_crit_tracks
            min_station = [station]
            n_neighbours = len(para.network[station])
        elif n_crit_tracks == min:
            if len(para.network[station]) < n_neighbours:
                min = n_crit_tracks
                min_station = [station]
                n_neighbours = len(para.network[station])
            elif len(para.network[station]) == n_neighbours:
                min_station.append(station)
    return(random.choice(min_station))
