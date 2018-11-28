import random


def start_select(network, L_crit_tracks, stations):
    min_station = []
    for station in stations:
        n_crit_tracks = sum(track.count(station) for track in L_crit_tracks)
        if len(min_station) == 0:
            min_station = [station]
            min = n_crit_tracks
            n_neighbours = len(network[station])
        elif n_crit_tracks < min and n_crit_tracks > 0:
            min = n_crit_tracks
            min_station = [station]
            n_neighbours = len(network[station])
        elif n_crit_tracks == min:
            if len(network[station]) < n_neighbours:
                min = n_crit_tracks
                min_station = [station]
                n_neighbours = len(network[station])
            elif len(network[station]) == n_neighbours:
                min_station.append(station)
    return(random.choice(min_station))
