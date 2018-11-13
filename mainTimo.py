# Imports
import os, sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

import random_route as rand
import create_starts as cs
import network as nw
import station_class as st
import import_data as imp

import_dict= imp.open_stations('data','StationsHolland.csv')
import_list= imp.open_connections('data','ConnectiesHolland.csv')
station_dict=imp.add_connections_dict(import_dict,import_list)

stations={}
for x in station_dict:
    location= [station_dict[x]['Longitude'],station_dict[x]['Latitude']]
    stations[x] = st.Station(x,x,station_dict[x]['Critical'],location,station_dict[x]['Neighbours'])

print(stations['Alkmaar'].information());

G = nw.Network_Graph(st.Station).graph

starts = cs.create_starts(G, 7)
print(starts)
for x in starts:
    print(rand.random_route(G, x, 120))
