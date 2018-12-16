def transform(graph, tracks):
    """Gets list of list of tracks and returns same list of list but with
    aditional information"""
    transform = []
    min_list = []
    total_time = 0
    for track in tracks:
        tracklist = []
        track_time = 0
        for i in range(len(track)):
            if i+1 < len(track):
                a = track[i]
                b = track[i+1]
                time = int(float(graph[a][b]['weight']))
                tracklist.append([[a, b], time])
                track_time += time
        tracklist = [tracklist, track_time]
        transform.append(tracklist)
        min_list.append(track_time)
        total_time += track_time
    return transform, total_time, min_list
