import transform_tracklist as tt
import random_route as rr
import routes as rt
import copy
from random import randint


def score_impr(graph, tracks, apct, uct):
    bkv = []                 # bereden kritieke verbindingen
    transformed = tt.transform(graph, tracks)[0]
    time = tt.transform(graph, tracks)[1]
    # minlist = tt.transform(graph, tracks)[2]
    t = len(tracks)
    for i in range(t):
        track = transformed[i][0]
        clist = [x for x in track if x in apct]
        for x in clist:
            inverse_x = [[x[0][1], x[0][0]], x[1]]
            if x not in bkv:
                if inverse_x not in bkv:
                    bkv.append(x)
    p = len(bkv)/len(uct)
    S = p*10000 - (t*20 + time/10)
    return S


class Trajects():
    def __init__(self, graph, tracks):
        self.graph = graph
        self.tracks = tracks

    def information(self):
        return '{} {}'.format('Tracks: ', self.tracks)

    def score(self, apct, uct):
        bkv = []                 # bereden kritieke verbindingen
        transformed = tt.transform(self.graph, self.tracks)[0]
        time = tt.transform(self.graph, self.tracks)[1]
        # minlist = tt.transform(graph, tracks)[2]
        t = len(self.tracks)
        for i in range(t):
            track = transformed[i][0]
            clist = [x for x in track if x in apct]
            for x in clist:
                inverse_x = [[x[0][1], x[0][0]], x[1]]
                if x not in bkv:
                    if inverse_x not in bkv:
                        bkv.append(x)
        p = len(bkv)/len(uct)
        S = p*10000 - (t*20 + time/10)
        return S  # , p, len(bkv), len(uct), time

    def transform_track(self, track_x, cut_x, minutes, apct, uct):
        copy_tracks = copy.copy(self.tracks)
        transform_track = self.tracks[track_x]

        first_part_incl_cut = transform_track[:cut_x]
        first_part = first_part_incl_cut[:-1]

        transformed_tracklist = tt.transform(self.graph, [first_part])
        time_first_part = transformed_tracklist[1]
        cut_station = transform_track[cut_x-1+len(transform_track)]

        new_part = rr.random_route(self.graph, cut_station, minutes-time_first_part, first_part_incl_cut)
        transformed_track = new_part
        copy_tracks[track_x] = transformed_track


        old_score = score_impr(self.graph, self.tracks, apct, uct)
        new_score = score_impr(self.graph, copy_tracks, apct, uct)

        return [copy_tracks, new_score, old_score]

    def transform_track_return_if_impr(self, track_x, cut_x, minutes, apct, uct):
        copy_tracks = copy.copy(self.tracks)
        transform_track = self.tracks[track_x]

        first_part_incl_cut = transform_track[:cut_x]
        first_part = first_part_incl_cut[:-1]

        transformed_tracklist = tt.transform(self.graph, [first_part])
        time_first_part = transformed_tracklist[1]
        cut_station = transform_track[cut_x-1+len(transform_track)]
        new_part = rr.random_route(self.graph, cut_station, minutes-time_first_part, first_part_incl_cut)
        # new_part = rt.random_track(self.graph, cut_station, minutes-time_first_part)
        # new_part2 = rt.combine_all_timelimit(self.graph, cut_station, minutes-time_first_part)
        # rlen = len(new_part2)
        # random_index = randint(0, rlen-1)
        # print(len(new_part2), random_index, new_part2[random_index])
        transformed_track = new_part

        copy_tracks[track_x] = transformed_track


        old_score = score_impr(self.graph, self.tracks, apct, uct)
        new_score = score_impr(self.graph, copy_tracks, apct, uct)

        if new_score > old_score:
            return [copy_tracks, new_score, old_score]
        else:
            pass




# ['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal'],
# ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Delft'],
# ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']
