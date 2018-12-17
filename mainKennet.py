# Imports
import os
import sys

# de map waarin het project staat
located_map = "TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")
sys.path.append(parent_dir_name+"\\"+located_map+"\\code\\class")

# test
print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code")


# import bestanden vanuit de map code
import network as nw
import import_data as imp
import station_class as st
import breadth_first_search as bfs
import routes as rt
import traject_class as tc
import score as sc
import random_route as rr
import decimal
import transform_tracklist as tt
import hillclimber_obj_orien as hh
import simulated_annealing as sa


# import files using the functions from import_data.py
import_name = "Nationaal"

if import_name == "Holland":
    import_dict = imp.open_stations('data', 'StationsHolland.csv')
    import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
if import_name == "Nationaal":
    import_dict = imp.open_stations('data', 'StationsNationaal.csv')
    import_list = imp.open_connections('data', 'ConnectiesNationaal.csv')


station_dict = imp.add_connections_dict(import_dict, import_list)


# adding the stations as instances of the class Station
stations = {}
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                             station_dict[x]['Neighbours'])

print(station_dict)

for x in stations:
    if 'Amsterdam' in stations[x].label:
        stations[x].update_single('Amsterdam', 'A.')
    if 'Rotterdam' in stations[x].label:
        stations[x].update_single('Rotterdam', 'R.')
    if 'Den Haag' in stations[x].label:
        stations[x].update_single('Den Haag', 'DH.')


# test the class Station
print(stations['Amsterdam Centraal'].information())


# test network.py
G = nw.Network_Graph(st.Station)
print(G.information())

apct = sc.unique(station_dict)[0]
uct = sc.unique(station_dict)[1]

testT = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem'], ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Delft'], ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']]
testT2 = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Amsterdam Zuid', 'Schiphol Airport', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander'],['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem'],['Heerlen', 'Sittard', 'Roermond','Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Leiden Centraal', 'Den Haag Laan v NOI'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Ede-Wageningen', 'Arnhem Centraal', 'Nijmegen', 'Oss'],['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum'],['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Blaak', 'Dordrecht', 'Roosendaal', 'Etten-Leur', 'Breda'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum'],['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal', 'Schiphol Airport', 'Leiden Centraal', 'Den Haag HS', 'Gouda', 'Den Haag Centraal']]

testT2 = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Amsterdam Zuid', 'Schiphol Airport', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander'],['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem'],['Heerlen', 'Sittard', 'Roermond','Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Leiden Centraal', 'Den Haag Laan v NOI'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Ede-Wageningen', 'Arnhem Centraal', 'Nijmegen', 'Oss'],['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum'],['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Blaak', 'Dordrecht', 'Roosendaal', 'Etten-Leur', 'Breda'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum'],['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal', 'Schiphol Airport', 'Leiden Centraal', 'Den Haag HS', 'Gouda', 'Den Haag Centraal']]

testT3 = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel'],['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Utrecht Centraal'],['Heerlen', 'Sittard', 'Roermond','Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Ede-Wageningen', 'Arnhem Centraal', 'Nijmegen', 'Oss'],['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal'],['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Gouda', 'Rotterdam Alexander'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum'],['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal', 'Schiphol Airport', 'Leiden Centraal']]

testT4 = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem'],['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven'],['Heerlen', 'Sittard', 'Roermond','Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal'],['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal'],['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort'],['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal']]

testT5 = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk'],
['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven'],
['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren'],
['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk'],
['Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum'],
['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle'],
['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal'],
['Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum']]


testT51 = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'],
['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum'],
['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Gouda'],
['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Laan v NOI'],
['Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss', 'Nijmegen', 'Arnhem Centraal'],
['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle'],
['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal', 'Dordrecht', 'Rotterdam Blaak', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Gouda', 'Den Haag Centraal'],
['Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum']]
# T = tc.Trajects(G.graph, testT4)
# print(T.information())
# print(G.graph['Heemstede-Aerdenhout'])
# testscore = T.score(apct, uct)
# print(T.score(apct, uct))
#
# X = tc.Trajects(G.graph, testT2)
# print(X.score(apct, uct))
# highscore = 0
# for a in range(8):
#     for b in range(200):
#         print(a, b)
#         Y = tc.Trajects(G.graph, T.transform_track(a, -5, 180))
#         y_score = Y.score(apct, uct)
#         if y_score > testscore:
#             print(Y.score(apct, uct), Y.information())
#             if y_score > highscore:
#                 highscore = y_score
#                 Y_high = Y
#     print(Y_high, highscore)
#
# print(Y_high, highscore)

# for a in range(3):
#     print(T.transform_track_return_if_impr(0, -1, 180, apct, uct))
w_tracks =  [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'], ['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Oss', 'Nijmegen', 'Arnhem Centraal'], ['Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Blaak', 'Dordrecht', 'Roosendaal'], ['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Centraal', 'Gouda', 'Den Haag HS'], ['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum'], ['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Hilversum'], ['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Schiphol Airport', 'Leiden Centraal', 'Den Haag Laan v NOI'], ['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum']]

w_sa= [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Gouda'], ['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Blaak', 'Schiedam Centrum', 'Rotterdam Centraal', 'Schiedam Centrum'], ['Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Utrecht Centraal', 'Ede-Wageningen', 'Arnhem Centraal', 'Nijmegen', 'Oss', 's-Hertogenbosch', 'Tilburg'], ['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk'], ['Steenwijk', 'Zwolle', 'Deventer', 'Apeldoorn', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum', 'Amsterdam Amstel', 'Amsterdam Zuid', 'Schiphol Airport', 'Leiden Centraal'], ['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Utrecht Centraal', 'Gouda', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Den Haag Laan v NOI'], ['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Alphen a/d Rijn'], ['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Rotterdam Blaak']]

W = tc.Trajects(G.graph, testT5)
print(W.information())


# g_tracks = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout'], ['Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Beverwijk'], ['Alphen a/d Rijn', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum'], ['Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Zaandam', 'Hoorn', 'Alkmaar'], ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Zaandam', 'Beverwijk', 'Castricum', 'Alkmaar', 'Castricum', 'Alkmaar']]
# W = tc.Trajects(G.graph, g_tracks)

#  hillclimber!!!!!!!!!!
# def hillclimber(graph, traject, nr_tracks, iterations, cut_x, minutes, apct, uct):
#     highscore = 0
#     total_i = 0
#     score_i_list = []
#     for a in range(nr_tracks):
#         print(a, 'len of track:', len(traject.tracks[a]))
#         for b in range(iterations):
#             total_i += 1
#             new = traject.transform_track_return_if_impr(a, cut_x, minutes, apct, uct)
#             if new != None:
#                 new_tracks = new[0]
#                 new_score = new[1]
#                 score_i_list.append([total_i,new_score])
#                 if new_score > highscore:
#                     Y = tc.Trajects(graph.graph, new_tracks)
#                     highscore = new_score
#                     print(a,b,new_score,highscore, new_tracks[a])
#         # if 'Y' in locals():
#                     traject = Y
#     for ab in score_i_list:
#         print(ab)
#     return traject


# new_track = hh.hillclimber(G, W, 8, 1000, -3, 180, apct, uct)[0].tracks
# print(new_track)
# print(sc.score(G.graph,new_track,apct,uct)[0])
# G.draw_choice(['all tracks',tt.transform(G.graph,new_track)[0],uct],egdes_option=False)
#
# W5= tc.Trajects(G.graph, testT51)
# G.draw_choice(['all tracks', tt.transform(G.graph,W5.tracks)[0],uct],egdes_option=False)
# L.draw_choice(['track',tt.transform(L.graph,endtest)[0],uct],egdes_option=False)

# from math import exp
#
#
# def acceptance_probability(old_score, new_score, T):
#     score_dif = (new_score-old_score)
#     tt = (9400-old_score)/100
#     a = exp(score_dif/20)
#     return a
#
# from random import random
#
#
# def simulated_annealing(graph, traject, nr_tracks, iterations, cut_x, minutes):
#     for a in range(nr_tracks):
#         print(a, 'len of track: ', len(traject.tracks[a]))
#         old_score = traject.score(apct, uct)
#         T = 1.0
#         T_min = 0.1
#         alpha = 0.8
#         while T > T_min:
#             i = 1
#             while i <= iterations:
#                 new_sol = traject.transform_track(a, cut_x, minutes, apct, uct)
#                 new_score = new_sol[1]
#                 ap = acceptance_probability(old_score, new_score, T)
#                 r = random()
#                 if ap > r:
#                     sol = new_sol
#                     print(i, round(ap,2), round(r,2), new_score, new_score-old_score)
#                     old_score = new_score
#                     # traject = tc.Trajects(graph.graph, sol[0])
#
#                 i += 1
#             print(a,T)
#             T = T*0.8
#         if 'sol' in locals():
#             traject = tc.Trajects(graph.graph, sol[0])
#             print(traject.information())
#     return sol


print(sa.simulated_annealing(G, W, 8, 100, -3, 180,apct, uct).tracks)
endtest3 = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'],['Maastricht', 'Sittard', 'Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 's-Hertogenbosch', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum'],['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Ede-Wageningen', 'Utrecht Centraal', 'Gouda'],['Hoorn', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 'Alphen a/d Rijn', 'Leiden Centraal', 'Den Haag Laan v NOI'],['Steenwijk', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Hilversum', 'Utrecht Centraal', 's-Hertogenbosch', 'Oss', 'Nijmegen', 'Arnhem Centraal'],['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle'],['Helmond', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Roosendaal', 'Dordrecht', 'Rotterdam Blaak', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag HS', 'Gouda', 'Den Haag Centraal'],['Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum']]
print(sc.score(G.graph,new_track,apct,uct)[0])
# L.draw_choice(['track',tt.transform(L.graph,endtest)[0],uct],egdes_option=False)
G.draw_choice(['all tracks',tt.transform(G.graph,new_track)[0],uct],egdes_option=False)

# IMPORTA ;KASDNF;LAJ S;FLKJ ASPDLFKJ PASLKDGJ PASRHG
print(1111111111111111111111111)
# print(W.transform_track(0, -4, 180, apct, uct))

# print(W.information())
# btrack = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Gouda', 'Utrecht Centraal', 'Amsterdam Centraal'], ['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag HS', 'Leiden Centraal', 'Den Haag Centraal'], ['Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'], ['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Almere Centrum', 'Hilversum', 'Utrecht Centraal'], ['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Nijmegen', 'Oss', 's-Hertogenbosch', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Breda'], ['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum'], ['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Centraal', 'Amsterdam Sloterdijk'], ['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal']]
# ctrack = [['Den Helder', 'Alkmaar', 'Castricum', 'Beverwijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag HS', 'Delft', 'Den Haag Centraal', 'Gouda', 'Utrecht Centraal', 'Amsterdam Centraal'], ['Maastricht', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag HS', 'Leiden Centraal', 'Den Haag Centraal'], ['Heerlen', 'Sittard', 'Roermond', 'Weert', 'Eindhoven', 'Tilburg', 'Breda', 'Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid'], ['Enschede', 'Hengelo', 'Almelo', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Almere Centrum', 'Hilversum', 'Utrecht Centraal'], ['Steenwijk', 'Zwolle', 'Deventer', 'Zutphen', 'Dieren', 'Arnhem Centraal', 'Nijmegen', 'Oss', 's-Hertogenbosch', 'Eindhoven', 'Tilburg', 'Breda', 'Etten-Leur', 'Breda'], ['Hoorn', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Schiphol Airport', 'Utrecht Centraal', 'Amsterdam Centraal', 'Almere Centrum'], ['Heerenveen', 'Leeuwarden', 'Groningen', 'Assen', 'Zwolle', 'Amersfoort', 'Utrecht Centraal', 'Amsterdam Centraal', 'Amsterdam Sloterdijk'], ['Helmond', 'Eindhoven', 'Tilburg', 's-Hertogenbosch', 'Utrecht Centraal', 'Ede-Wageningen','Arnhem Centraal', 'Nijmegen','Oss']]
#
# B = tc.Trajects(G.graph, btrack
# C = tc.Trajects(G.graph, ctrack)
#
# print(B.score(apct, uct))
# print(C.score(apct, uct))

#             if y_score > testscore:
#                 print(Y.score(apct, uct), Y.information())
#                 if y_score > highscore:
#                     highscore = y_score
#                     Y_high = Y
#                 print(Y_high, highscore)
#
# print(Y_high, highscore)




# print(G.calc_statespace('Holland'))
# print('')
# print(G.calc_statespace('Nationaal'))

# G.graph.nodes()

# adam_bfs = bfs.pathcount(G.graph, 'Amsterdam Centraal', 20)
# for x in adam_bfs:
#     print(x, adam_bfs[x])


# for x in rt.all_shortest_nodes(G.graph, 'Amsterdam Centraal', 120):
#     print(x)

# sort_routes = sorted(rt.all_shortest_nodes(G.graph, 'Amsterdam Centraal',
#                      120), key=lambda x: x[1])
# for x in sort_routes:
#     print(x)



# apct= sc.unique(station_dict)[0]
# uct= sc.unique(station_dict)[1]
#
# solution_track=[['Dordrecht', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel'], ['Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Beverwijk', 'Zaandam', 'Castricum', 'Alkmaar', 'Hoorn'], ['Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn'], ['Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Sloterdijk', 'Zaandam', 'Hoorn', 'Alkmaar', 'Den Helder']]
# solution_track1=[['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal', 'Delft', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn'], ['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk'], ['Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Dordrecht'], ['Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']]
# solution_track2=['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal'],['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Delft'],['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']
# print(sc.score(L.graph,solution_track2,apct,uct))
# L.draw_choice(['track',tt.transform(L.graph,solution_track2)[0]],egdes_option=False)
# L.draw_choice(['all tracks',tt.transform(L.graph,solution_track2)[0],uct],egdes_option=False)
