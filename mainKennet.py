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

# import files using the functions from import_data.py
import_dict = imp.open_stations('data', 'StationsHolland.csv')
import_list = imp.open_connections('data', 'ConnectiesHolland.csv')
station_dict = imp.add_connections_dict(import_dict, import_list)


# adding the stations as instances of the class Station
stations = {}
for x in station_dict:
    location = [station_dict[x]['Longitude'], station_dict[x]['Latitude']]
    stations[x] = st.Station(x, x, station_dict[x]['Critical'], location,
                             station_dict[x]['Neighbours'])


# test the class Station
print(stations['Alkmaar'].information())


# test network.py
G = nw.Network_Graph(st.Station)
print(G.information())

testT = [['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal'], ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Delft'], ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']]
T = tc.Trajects(G.graph, testT)
print(T.transform_track(0, -3))

print(G.calc_statespace('Holland'))
print('')
print(G.calc_statespace('Nationaal'))

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
