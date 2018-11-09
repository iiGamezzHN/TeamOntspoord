import pandas as pd

def open_stations2(location,file):
    """ Deze functie heeft de locatie en de naam van de databestand als input
    en geeft als output ...
    """
    df= pd.read_csv(location+"/"+file,names=["Station","Latitude","Longitude","Critical"])

    stations= df['Station']
    stations_critical= df[df.Critical=='Kritiek']["Station"].tolist()
    stations_ncritical= df[df.Critical!='Kritiek']["Station"].tolist()
    # set the column 'Station' as index, then create a dict with the index (station) as key
    # and the other columns as values
    # example > {'stationA': {'Latitude': 52.63777924, 'Longitude': 4.739722252, 'Critical': 'Kritiek'}, ...}
    station_dict= df.set_index('Station').to_dict('index')
    return station_dict

    # for i in range(len(df)):
    #     station= df["Station"][i]
    #     station_loc_dict[station]
    #     print(df['Station'][i])



def open_connections2(location,file):
    df= pd.read_csv(location+"/"+file,names=["StationA","StationB","Minutes"])
    connection_list=[]

    for i in range(len(df)):
        connection_list.append([df['StationA'][i],df['StationB'][i],df['Minutes'][i]])

    print(connection_list)
    return connection_list

def add_connections_dict(dict,list):
    neighboursDict={}
    for station in dict:
        for y in list:
            if station==y[0]:
                station_neighbours.append([y[1],y[2]])
            elif station==y[1]:
                station_neighbours.append([y[0],y[2]])
                
