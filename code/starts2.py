import random


def start_select(G, L_crit_tracks, stations):
    min_station = []
    for station in stations:
        x = sum(track.count(station) for track in L_crit_tracks)
        if len(min_station) == 0:
            min_station = [station]
            min = x
        if x < min and x > 0:
            min = x
            min_station = [station]
        elif x == min:
            min_station.append(station)
    return(random.choice(min_station))
