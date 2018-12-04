# The imports
import pandas as pd


def open_stations(location, file):
    """ Deze functie heeft de locatie (folder) en de naam van de file als input
    en geeft als output een dict van de stations (zonder neighbours!)
    example > {'stationA': {'Latitude': 52.6, 'Longitude': 4.7,
    'Critical': 'Kritiek'}, ...} """
    df = pd.read_csv(location+"/"+file, names=["Station", "Latitude",
                                               "Longitude", "Critical"])
    station_dict = df.set_index('Station').to_dict('index')
    return station_dict


def open_connections(location, file):
    """ Deze functie heeft de locatie (folder) en de naam van de file als input
    en geeft als output de connection_list. example > [['Den Haag
    Centraal', 18], ['Alphen a/d Rijn', 19], ['Rotterdam Alexander', 10]
    , ...] """
    df = pd.read_csv(location+"/"+file, names=["StationA", "StationB",
                                               "Minutes"])
    connection_list = []
    for i in range(len(df)):
        connection_list.append([df['StationA'][i], df['StationB'][i],
                                df['Minutes'][i]])
    return connection_list


def add_connections_dict(dict, list):
    """ Deze functie heeft de locatie (folder) en de naam van de data-
    bestand als input en geeft als output een dict van de stations (met
    neighbours!) example > {'stationA': {'Latitude': 52.6, 'Longitude':
    4.72, 'Critical': 'Kritiek', 'Neighbours':[[stationC,13],[stationD,
    20]]}, ...}"""
    neighbours_dict = {}
    for station in dict.keys():
        station_neighbours = []
        for y in list:
            if station == y[0]:
                station_neighbours.append([y[1], y[2]])
            elif station == y[1]:
                station_neighbours.append([y[0], y[2]])
        neighbours_dict['Neighbours'] = station_neighbours

        temp_dict = dict[station]
        temp_dict['Neighbours'] = neighbours_dict['Neighbours']
        dict[station] = temp_dict
    return dict
