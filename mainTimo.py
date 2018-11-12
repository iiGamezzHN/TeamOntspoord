# Imports
import os, sys
import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd


INPUT_CSV1 = 'StationsHolland.csv'
INPUT_CSV2 = 'ConnectiesHolland.csv'

df= pd.read_csv('data/StationsHolland.csv', header=None) #Load the Parkline data into a dataframe
df2= pd.read_csv("data/ConnectiesHolland.csv")

G = nx.Graph()

with open(INPUT_CSV1, newline='') as in_csv1:
        line_count = 0
        stations = csv.reader(in_csv1)
        for item in stations:
            G.add_node(item[0], name = item[0], x = 'x')

with open(INPUT_CSV2, newline='') as in_csv2:
    connections = csv.reader(in_csv2)
    for item in connections:
        G.add_edge(item[0],item[1],weight = item[2])



plt.plot()
labels= nx.get_edge_attributes(G, 'weight')
nx.draw(G, with_labels=True)

#plt.show()
# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

import random_route as rand
import create_starts as cs

starts = cs.create_starts(G, 7)
for x in starts:
    print(rand.random_route(G, x, 120))
