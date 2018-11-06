# Imports
import os, sys

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

# test
print(parent_dir_name)
print(parent_dir_name+"\\"+located_map+"\\code" )

# import bestanden vanuit de map code
import network as nw
import import_data as imp

nw.import_other_func()

imp.open_connections('data','ConnectiesHolland.csv')

imp.open_stations('data','StationsHolland.csv')
