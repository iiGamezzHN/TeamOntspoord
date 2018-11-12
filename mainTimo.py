# Imports
import os, sys
import networkx as nx

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

# test
print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code" )



# import bestanden vanuit de map code
#import network as nw
#import functiesDavid as func
import random_route as rand
import import_data as imp

testdf= imp.open_stations('data','StationsHolland.csv')[1]
print(testdf)
#rand.random_route(G, 'Amsterdam Centraal', 120)
