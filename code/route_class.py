class Route():

    """Object saving all relevant data for current route"""

    def __init__(self, station, L_route, tot_weight, n_crit_tracks,
                                        L_crit_tracks, k_score_ind):
        self.station = station
        self.L_route = L_route
        self.tot_weight = tot_weight
        self.n_crit_tracks = n_crit_tracks
        self.L_crit_tracks = L_crit_tracks
        self.k_score_ind = k_score_ind

    # Lets routes compare their k score
    def __gt__(self, other):
        return self.k_score_ind > other.k_score_ind

    def __lt__(self, other):
        return self.k_score_ind < other.k_score_ind
