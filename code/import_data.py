# The imports
import pandas as pd

def open_stations(location,file):
    """ Deze functie heeft de locatie en de naam van de databestand als input
    en geeft als output ...
    """
    df= pd.read_csv(location+"/"+file,names=["Station","Latitude","Longitude","Critical"])

    stations= df['Stations']
    stations_critical= df[df.Critical=='Kritiek']["Station"].tolist()
    stations_ncritical= df[df.Critical!='Kritiek']["Station"].tolist()

    for i in range(len(df)):
        station= df["Station"][i]
        station_loc_dict[station]
        print(df['Station'][i])



def open_connections(location,file):
    df= pd.read_csv(location+"/"+file,names=["StationA","StationB","Minutes"])
    connection_list=[]

    for i in range(len(df)):
        connection_list.append(df)
