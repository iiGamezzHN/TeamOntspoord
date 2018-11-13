# Imports
import os, sys

# de map waarin het project staat
located_map="TeamOntspoord"

# pak de parent map
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name+"\\"+located_map+"\\code")

# test
#print(parent_dir_name)
#print(parent_dir_name+"\\"+located_map+"\\code" )

# import bestanden vanuit de map code
import functiesDavid as fd
import station_class as sc

connections = fd.open_connections('data','ConnectiesHolland.csv')
stations = fd.open_stations('data','StationsHolland.csv')[1]
stations_crit = fd.open_stations('data','StationsHolland.csv')[2]
con_dict = fd.add_connections_dict(stations, connections)
print(con_dict)
