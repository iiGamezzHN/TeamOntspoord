# Imports
import os
import sys

# de map waarin het project staat
located_map = "TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")
sys.path.append(parent_dir_name+"\\"+located_map+"\\code\\class")

# import bestanden vanuit de map code
import network as nw
import import_data as imp
import station_class as st
import calc_crit_tracks as ct
from starts2 import start_select as s2
from operator import itemgetter
import parameter_class as pc
import route_class as rc
import breadth_first_beam as bfb
import calc_route_score as crs
import score as sc
import score_nationaal as sc_n
import bfb_draw as draw

results = []

def breadth_first_beam_main(region, all_crit, depth, n_best):
    # import files using the functions from import_data.py
    import_dict = imp.open_stations('data', 'Stations'+region+'.csv')
    import_list = imp.open_connections('data', 'Connecties'+region+'.csv')
    station_dict = imp.add_connections_dict(import_dict, import_list)

    # adding the stations as instances of the class Station
    stations = {}
    list_stations = []
    for x in station_dict:
        location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
        stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                                 station_dict[x]['Neighbours'])
        list_stations.append(x)

    G = nw.Network_Graph(st.Station).graph

    if region == "Holland":
        max_length = 120
        nr_tracks = 7
    elif region == "Nationaal":
        max_length = 180
        nr_tracks = 20

    list_crit_tracks = ct.crit_tracks(G, region, all_crit)
    tot_crit_tracks = len(list_crit_tracks)
    parameters = pc.Parameters(G, max_length, tot_crit_tracks, list_stations)
    start = s2(parameters, list_crit_tracks)
    route = rc.Route(start, [start], 0, 0, list_crit_tracks, 0, 0)

    tracks = []
    var = 0

    while True:
        final_routes = bfb.main(G, [route], depth, station_dict, list_crit_tracks,
                                max_length, n_best)
        sorting = []
        for x in final_routes:
            sorting.append(x.k_score_ind)
        sorting = sorted(sorting, reverse=True)

        final_track = []
        station = final_routes[0].station
        L_route = final_routes[0].L_route
        tot_weight = final_routes[0].tot_weight
        n_crit_tracks = final_routes[0].n_crit_tracks
        L_crit_tracks = final_routes[0].L_crit_tracks
        k_score_ind = final_routes[0].k_score_ind
        final_track.append(rc.Route(station, L_route, tot_weight,
                           n_crit_tracks, L_crit_tracks, k_score_ind, 0))

        a = crs.pair_stations([final_track[0].L_route])

        for x in a:
            for y in list_crit_tracks:
                if x[0] in y and x[1] in y:
                    list_crit_tracks.remove(y)

        final_track[0].L_crit_tracks = list_crit_tracks

        tracks.append(final_track[0].L_route)

        # print("")
        # print(final_track[0].L_route)
        # print(final_track[0].tot_weight)
        # print(final_track[0].k_score_ind)
        # print(len(final_track[0].L_crit_tracks))
        # print(final_track[0].L_crit_tracks)
        # print("")

        if len(tracks) == nr_tracks:
            break

        if len(list_crit_tracks) == 0:
            break

        tot_crit_tracks = len(list_crit_tracks)
        parameters = pc.Parameters(G, max_length, tot_crit_tracks, list_stations)
        start = s2(parameters, list_crit_tracks)
        route = rc.Route(start, [start], 0, 0, list_crit_tracks, 0, 0)

        var += 1

    # print('len tracks', len(tracks))
    # print('tracks', tracks)

    if all_crit:
        unique = sc_n.unique(station_dict)
        score = sc_n.score(G, tracks, unique[0], unique[1])
        print('crit')
        # print(score)
    else:
        unique = sc.unique(station_dict)
        score = sc.score(G, tracks, unique[0], unique[1])
    # print(score)
    #
    # list_crit_tracks2 = ct.crit_tracks(G, 'Holland', True)
    # a = sc_n.calc_score(G, tracks, sc_n.unique(station_dict)[1], sc_n.unique(station_dict)[1])
    # print(a)


    return [score, depth, n_best, len(tracks), tracks]


# lala = breadth_first_beam_main("Holland", True, 4, 10)
# print(lala)

for x in range(3, 8, 2):  # Get scores for different variables of depth, n_best
    for y in range(5, 31, 5):
        print(x, y)
        result = breadth_first_beam_main("Holland", False, x, y)
        # print(result)
        results.append(result)

print(results)
# results = sorted(results, key=itemgetter(0), reverse=True)
print("")

val1 = []
val2 = []
val3 = []
used_depth = []  # Objects in draw
# for i in range(5, 6):
for x in results:
    if x[1] == 3:
        print(x)
        used_depth.append(x[2])
        val1.append(x[0][0])
    elif x[1] == 5:
        print(x)
        val2.append(x[0][0])
    elif x[1] == 7:
        print(x)
        val3.append(x[0][0])

min = val1[-1] - 200

# print(best)

draw.draw2(used_depth, val1, min, val2, val3)  # Uncomment to draw

# for x in results:
#     if x[1] == 3:
#         print(x)
#         used_depth.append(x[2])
#         val1.append(x[0][0])
#     elif x[1] == 5:
#         print(x)
#         val2.append(x[0][0])
#     elif x[1] == 7:
#         print(x)
#         val3.append(x[0][0])

# with open('BFB_.txt', 'w') as f:
#     for item in results:
#         f.write("%s\n" % item)
#     asdf = str(sc.score(G, tracks, unique[0], unique[1]))
#     f.write(asdf)
