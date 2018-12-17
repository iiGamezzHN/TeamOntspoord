This folder contains all functions and classes that are used in main.py.

starts2.py calculates the optimal starting point with the remaining critical
tracks. It does this by picking a station with the fewest critical connections,
then fewest connections, then longest critical connection.

depth_first_n_best gives starting from a given starting station, given network,
and given maximum length of a route a list of the n_best best routes. Best
routes are calculated by calculating the k-score of every route.

lookahead_for_depth_first tries to slowly increase the final k-score. This is
done by generating a list of best routes with route2_object_n_best, and then
for each route continue calculating the best (nr. 1) routes until no more
critical tracks remain. Once that is done, you pick the first route with the
highest final k-score. Then it does this same process for track nr. 2, 3 etc.

#### breadth_first_beam
Update_tracks voegt 'oude' en 'nieuwe' routes aan elkaar toe zodat het 1 gehele route wordt.

Bfb is de fuctie die de breadth first search met beam (vooruitkijken) uitvoert. Het returnt een x aantal routes vanuit het beginpunt (beginpunten)
als de ingestelde diepte van de beam bereikt is.

Main is de fuctie die zorgt dat bfb runt totdat de maximale lengte van de route is bereikt. Hij returnt de nieuwe lijst met routes wanneer
alle routes boven het minimale aantal minuten zitten.

#### calc_route_score
Calc_route_score roept calc_score aan om de score te berekenen van de routes. Wanneer zo'n route langer is dat het maximaal toegestane minuten
voor een traject haalt hij net zo lang een laatste traject er af totdat de lengte onder de max van minuten zit. Dan pakt hij de routes en haalt
de dubbele routes er uit. Waarna hij de lijst sorteert van hoog naar laag op de score. Hierna returnt hij deze lijst met de n_best scores.

Calc_score pakt de trajecten uit de volledige route en kijkt of er trajecten kritiek zijn. Vervolgens pakt hij van alle trajecten de tijd en
gebruikt dit om de score te berekenen. Hij returnt dan de route met de bijbehorende score, en tijd.

Pair_stations pakt de volledige route en maakt er losstaande trajecten van. Dus van ['Alkmaar','Castricum','Hoorn'] naar [['Alkmaar','Castricum'],['Castricum','Hoorn']]
