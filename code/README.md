This folder contains all functions and classes that are used in main.py.

starts2.py calculates the optimal starting point with the remaining critical
tracks. It does this by picking a station with the fewest critical connections,
then fewest connections, then longest critical connection.

route2_object_n_best gives starting from a given starting station, given network,
and given maximum length of a route a list of the n_best best routes. Best
routes are calculated by calculating the k-score of every route.

hillclimber_for_route2 tries to slowly increase the final k-score. This is
done by generating a list of best routes with route2_object_n_best, and then
for each route continue calculating the best (nr. 1) routes until no more
critical tracks remain. Once that is done, you pick the first route with the
highest final k-score. Then it does this same process for track nr. 2, 3 etc.
