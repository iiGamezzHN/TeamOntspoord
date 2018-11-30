class Parameters():

    """Object saving all parameters for calculation"""

    def __init__(self, network, max_length, tot_crit_tracks, stations_list):
        self.network = network
        self.max_length = max_length
        self.tot_crit_tracks = tot_crit_tracks
        self.stations_list = stations_list
