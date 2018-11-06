import networkx as nx
import matplotlib as plt
import pandas as pd

df= pd.read_csv('StationsHolland.csv', header=None) #Load the Parkline data into a dataframe
df2= pd.read_csv("ConnectiesHolland.csv")

df.columns = ['Station','X','Y',"Kritiek"]
df2.columns = ['Station_A','Station_B','Minuten']

#df = df.where((pd.notnull(df)), "")
lijst = df.Station.tolist()
for i in range(len(lijst)):
    if 'Amsterdam' in lijst[i]:
        lijst[i] = 'A.'+lijst[i][9:]
    if 'Rotterdam' in lijst[i]:
        lijst[i] = 'R.'+lijst[i][9:]

df.Station = lijst

lijst = df2.Station_A.tolist()
for i in range(len(lijst)):
    if 'Amsterdam' in lijst[i]:
        lijst[i] = 'A.'+lijst[i][9:]
    if 'Rotterdam' in lijst[i]:
        lijst[i] = 'R.'+lijst[i][9:]

df2.Station_A = lijst

lijst = df2.Station_B.tolist()
for i in range(len(lijst)):
    if 'Amsterdam' in lijst[i]:
        lijst[i] = 'A.'+lijst[i][9:]
    if 'Rotterdam' in lijst[i]:
        lijst[i] = 'R.'+lijst[i][9:]

df2.Station_B = lijst

train_links = []

for index, row in df2.iterrows():
    train_links.append((row['Station_A'], row['Station_B']))

stations = df.Station.tolist()

kritiek = df[df.Kritiek == "Kritiek"].Station.tolist()
train_links_kritiek = []
stations_kritiek = []

for x in kritiek:
    for y in train_links:
        if x in y:
            train_links_kritiek.append(y)

for x in train_links_kritiek:
    for y in x:
        stations_kritiek.append(y)

stations_kritiek = set(stations_kritiek)

all_graph = nx.Graph()
all_graph.add_edges_from(train_links)
all_graph.add_nodes_from(stations)

nx.draw(all_graph, with_labels=True)
plt.show()

kritiek_graph = nx.Graph()
kritiek_graph.add_nodes_from(stations_kritiek)
kritiek_graph.add_edges_from(train_links_kritiek)

nx.draw(kritiek_graph, with_labels=True)
plt.show()

test = {}
for index, row in df.iterrows():
    test[row['Station']] = (row['Y'],row['X'])

# for x in test:
#     print(x, test[x])

G=nx.Graph()

for x in test:
    G.add_node(x, pos=test[x])

G.add_edges_from(train_links)
pos = nx.get_node_attributes(G,'pos')
plt.figure(3, figsize=(8,8))

nx.draw(G,pos, with_labels=True, node_size=150, font_size=12)
plt.show()

test2 = {}

for x in list(stations_kritiek):
    temp = df[df.Station == x]
    test2[temp.iloc[0]['Station']] = (temp.iloc[0]['Y'],temp.iloc[0]['X'])

H=nx.Graph()

for x in test2:
    H.add_node(x, pos=test[x])

H.add_edges_from(train_links_kritiek)
pos = nx.get_node_attributes(H,'pos')
plt.figure(3, figsize=(8,8))

nx.draw(H,pos, with_labels=True, node_size=150, font_size=12)
plt.show()