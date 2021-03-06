class Route():

    """Object saving all relevant data for current route.
    station: current station
    L_route: list of stations visited
    tot_weight: total length of route
    n_crit_tracks: number of critical tracks visited
    L_crit_tracks: list of critical tracks remaining
    k_score_ind: k score of route
    n_tracks_since_crit = number of tracks since critical track
    """

    def __init__(self, station, L_route, tot_weight, n_crit_tracks,
                 L_crit_tracks, k_score_ind, n_tracks_since_crit):
        self.station = station
        self.L_route = L_route
        self.tot_weight = tot_weight
        self.n_crit_tracks = n_crit_tracks
        self.L_crit_tracks = L_crit_tracks
        self.k_score_ind = k_score_ind
        self.n_tracks_since_crit = n_tracks_since_crit

    # Lets routes compare their k score
    def __gt__(self, other):
        return self.k_score_ind > other.k_score_ind

    def __lt__(self, other):
        return self.k_score_ind < other.k_score_ind
