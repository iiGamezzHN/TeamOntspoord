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
# import breadth_first_search as bfs
import station_class as st



testdict= imp.open_stations('data','StationsHolland.csv')
testlist= imp.open_connections('data','ConnectiesHolland.csv')

station_dict=imp.add_connections_dict(testdict,testlist)


stations={}
for x in station_dict:
    location= [station_dict[x]['Latitude'],station_dict[x]['Longitude']]
    stations[x] = st.Station(x,x,station_dict[x]['Critical'],location,station_dict[x]['Neighbours'])

# d1=[x for x in station_dict if station_dict[x]['Critical']=='Critical']
# print(len(d1),d1)

print(stations['Alkmaar'].information());
# adam_bfs= bfs.pathcount(L.graph,'Amsterdam Centraal',20)
# for x in adam_bfs:
# 	print(x,adam_bfs[x])
