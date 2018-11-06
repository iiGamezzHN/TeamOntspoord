# The imports
import pandas as pd

#..

def open_stations(location,file):
    df= pd.read_csv(location+"/"+file,names=["StationA","StationB","Minutes"])
    print(df)


def import_connections():
    pass
