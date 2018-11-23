class Route():

    """docstring for ClassName"""

    def __init__(self, station, L_route, tot_weight, n_crit_tracks, L_crit_tracks):
        self.station = station
        self.L_route = L_route
        self.tot_weight = tot_weight
        self.n_crit_tracks = n_crit_tracks
        self.L_crit_tracks = L_crit_tracks

        # def information(self):
		# return '{} {} {} {} {}'.format(self.name, self.label, self.importance, self.location, self.neighbours)
