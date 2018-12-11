import transform_tracklist as tt
import routes as rt

from random import randint


def get_time(track):
    pass


class Trajects():
    def __init__(self, graph, tracks):
        self.graph = graph
        self.tracks = tracks

    def information():
        pass

    def score():
        pass

    def transform_track(self, track_x, cut_x):
        transform_track = self.tracks[track_x]
        first_part = transform_track[:cut_x-1]
        transformed_tracklist = tt.transform(self.graph, [first_part])
        time_first_part = transformed_tracklist[1]
        cut_station = transform_track[cut_x-1+len(transform_track)]

        new_part = rt.random_track(self.graph, cut_station, 120-time_first_part)
        new_part2 = rt.combine_all_timelimit(self.graph, cut_station,57)
        rlen = len(new_part2)
        random_index = randint(0, rlen-1)
        # print(len(new_part2), random_index, new_part2[random_index])
        transformed_track = first_part + new_part2[random_index]
        print("Old track: ", transform_track)
        print("New track: ", transformed_track)

        return transformed_track




# ['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Haarlem', 'Heemstede-Aerdenhout', 'Leiden Centraal', 'Den Haag Centraal'],
# ['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Rotterdam Centraal', 'Rotterdam Alexander', 'Gouda', 'Alphen a/d Rijn', 'Gouda', 'Den Haag Centraal', 'Delft'],
# ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Hoorn', 'Alkmaar']
