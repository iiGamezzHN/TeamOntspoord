Deze map bevat alle functies en classes die gebruikt worden (al dan niet direct)
in main.py

#### starts2.py
Berekent het 'optimale' startpunt voor een nieuwe route met de overgebleven kritieke verbindingen.
Dit gebeurt door te kijken naar een station met de minste kritieke verbindingen (maar >0), daarna
de minste verbindingen en dan de langste kritieke verbinding.

#### depth_first_n_best
Geeft een lijst met de beste routes (hoogste k-scores) vanaf een gegeven beginpunt.

#### lookahead_for_depth_first
Probeert om langzamerhand de totale k-score te verbeteren. Dit wordt gedaan door depth_first_n_best
te gebruiken, en dan voor elke route te kijken naar wat er zou gebeuren als er verder wordt
gerekend door altijd de beste te kiezen, en dan daarmee weer het eerste traject te kiezen.

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

#### network.py
De class Network_Graph zorgt ervoor dat het netwerk van alle stations wordt geladen. Daarnaast bevat het de functies om labels van stations aan te passen. Denk hierbij
aan dat 'Amsterdam Centraal' 'A. Centraal' wordt. Vanuit het netwerk kan ook direct de statespace worden berekend, met als vereiste dat de databestanden van het desbetreffende
netwerk/statespace zijn ingeladen. Tot slot het netwerk verschillende visualisaties tonen met de functie draw_choice. Hierbij kan het volgende worden gevisualiseerd:
<br>- Het netwerk met de labels van alle edges en stations
<br>- Het netwerk met alleen de labels van de kritieke stations
<br>- Het netwerk met alleen de labels van de edges en stations van de route + de labels van de kritieke stations
<br>- Het netwerk met een counter op alle bereden edges, de edges met count=1 zijn groen, de andere edges verschillen in kleur rood>donkerrood
