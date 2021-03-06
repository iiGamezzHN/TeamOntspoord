import import_data as imp

"""
Returns a list of tuples, where elements are stations of a critical track.
"""


def crit_tracks(network, region, all):
    dict_stat = imp.open_stations('data', 'Stations' + region + '.csv')
    L_crit_stat = []
    L_crit_tracks = []
    # List of critical stations
    for item in dict_stat:
        if not all:
            if dict_stat[item]['Critical'] == 'Kritiek':
                L_crit_stat.append(item)
        else:
            L_crit_stat.append(item)
    # Adds critical tracks as tuples to list. Makes sure there are no doubles
    for x in L_crit_stat:
        for neighbour in network[x]:
            double = False
            for item in L_crit_tracks:
                if x in item and neighbour in item:
                    double = True
                    break
            if not double:
                L_crit_tracks.append([x, neighbour])
    return(L_crit_tracks)
