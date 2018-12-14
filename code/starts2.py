import random


def start_select(para, L_crit_tracks):
    """
    Select the 'best' starting station. Chooses the station with the fewest
    (but >0) critical connections. If equal, chooses station with fewest total
    connections. If equal, choose station with longest critical connection.
    If equal, chooses random.
    """
    min_station = []
    opt_weight = 0
    min = 99
    # Loop over all stations and check amount of crit connections
    for station in para.stations_list:
        n_crit_tracks = sum(track.count(station) for track in L_crit_tracks)
        crit_neighbours = []
        opt_weight_ind = 0
        for neighbour in para.network[station]:
            for track in L_crit_tracks:
                if neighbour in track and station in track:
                    crit_neighbours.append(neighbour)
        # Check for longest neighbouring critical track
        for item in crit_neighbours:
            distance = para.network[station][item]['weight']
            if distance > opt_weight_ind:
                opt_weight_ind = distance
        # Add if no stations have been found yet and if has critical track
        if len(min_station) == 0 and n_crit_tracks > 0:
            min_station = [station]
            min = n_crit_tracks
            n_neighbours = len(para.network[station])
            opt_weight = opt_weight_ind
        # Replace if station found with less critical tracks (but >0)
        elif n_crit_tracks < min and n_crit_tracks > 0:
            min_station = [station]
            min = n_crit_tracks
            n_neighbours = len(para.network[station])
            opt_weight = opt_weight_ind

        elif n_crit_tracks == min:
            # Checks for station with fewest total connections
            if len(para.network[station]) < n_neighbours:
                min = n_crit_tracks
                min_station = [station]
                n_neighbours = len(para.network[station])
                opt_weight = opt_weight_ind
            # Checks for longest critical track
            elif (len(para.network[station]) == n_neighbours and
                    opt_weight_ind > opt_weight):

                min = n_crit_tracks
                min_station = [station]
                n_neighbours = len(para.network[station])
                opt_weight = opt_weight_ind
            # If everything is equal add to list
            elif (len(para.network[station]) == n_neighbours and
                    opt_weight_ind == opt_weight):

                min_station.append(station)

    return(random.choice(min_station))
