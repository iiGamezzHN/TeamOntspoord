# The imports
import pandas as pd

def open_stations(location,file):
    """ Deze functie heeft de locatie (folder) en de naam van de file als input
    en geeft als output een dict van de stations (zonder neighbours!)
    example > {'stationA': {'Latitude': 52.63777924, 'Longitude': 4.739722252, 'Critical': 'Kritiek'}, ...}

    """
    df = pd.read_csv(location+"/"+file, names=["Station", "Latitude", "Longitude", "Critical"])
    stations = df['Station']
    # stations_critical= df[df.Critical=='Kritiek']["Station"].tolist()
    # stations_ncritical= df[df.Critical!='Kritiek']["Station"].tolist()
    # set the column 'Station' as index, then create a dict with the index (station) as key
    # and the other columns as values
    # example > {'stationA': {'Latitude': 52.63777924, 'Longitude': 4.739722252, 'Critical': 'Kritiek'}, ...}
    station_dict= df.set_index('Station').to_dict('index')
    return station_dict


def open_connections(location,file):
    """ Deze functie heeft de locatie (folder) en de naam van de file als input
    en geeft als output de connection_list
    example > [['Den Haag Centraal', 18], ['Alphen a/d Rijn', 19], ['Rotterdam Alexander', 10], ...]
    """
    df= pd.read_csv(location+"/"+file,names=["StationA","StationB","Minutes"])
    connection_list=[]
    for i in range(len(df)):
        connection_list.append([df['StationA'][i],df['StationB'][i],df['Minutes'][i]])
    return connection_list



def add_connections_dict(dict,list):
    """ Deze functie heeft de locatie (folder) en de naam van de databestand als input
    en geeft als output een dict van de stations (met neighbours!)
    example > {'stationA': {'Latitude': 52.63777924, 'Longitude': 4.739722252, 'Critical': 'Kritiek', 'Neighbours':[[stationC,13],[stationD,20],[stationE,24]]}, ...}
    """
    neighbours_dict={}
    for station in dict.keys():
        station_neighbours=[]
        for y in list:
            if station==y[0]:
                station_neighbours.append([y[1],y[2]])
            elif station==y[1]:
                station_neighbours.append([y[0],y[2]])
        neighbours_dict['Neighbours']=station_neighbours

        temp_dict= dict[station]
        temp_dict['Neighbours']= neighbours_dict['Neighbours']
        dict[station]=temp_dict
    return dict
