# TeamOntspoord - RailNL

Voor het project is gekozen voor het onderwerp RailNL, waarin een lijnvoering gemaakt moet worden voor de intercity treinen in
Nederland.

In deel 1 van de opdracht moet er er lijnvoering gemaakt worden voor Noord- en Zuid Holland.
De Scorefunctie is K = 10000 * p - (T*20 + Min/10). Hierbij is p de fractie van het aantal bereden kritieke trajecten, T het aantal gebruikte Tracks en Min het totaal aantal minuten van alle Tracks bij elkaar.
```
K = 10000 * p - (T*20 + Min/10)
```

## Aan de slag
### Deel 1
#### State Space
De state space wordt berekend door het volgende:

```
Formule ((s*n)^rpt/rtts)
```

Holland
<br>Totaal aantal stations(s):                      22
<br>Maximaal aantal buren voor een station(n):      4
<br>Minimale reistijd tussen twee stations(rtts):   5
<br>Maximale reistijd per traject(rpt):             120
<br>Maximaal aantal trajects:                       7

```
((22*4)^(120/5))^n
= ((22*4)^24) + ((22*4)^24)^2 + ((22*4)^24)^3 + ...... + ((22*4)^24)^7
= 2.73 e^108
```

#### Score Lower- en Upperbound
De absolute Lower en Upper bound voor 1b:
```
K: p = 0; T = 7; Min = 840 = -244       K: p = 1; T = 3; Min = 287; = 9911.3
```
De realistische Lower en Upper bound voor 1b:
```
K: p = 1; T = 7; Min = 840 = 9776.0     K: p = 1; T = 3; Min = 287; = 9911.3
```
De absolute Lower en Upper bound voor 1c:
```
K: p = 0; T = 7; Min = 840 = -244       K: p = 1; T = 4; Min = 381;
```
De realistische Lower en Upper bound voor 1c:
```
K: p = 1; T = 7; Min = 840 = 9776.0     K: p = 1; T = 4; Min = 381; = 9881.9
```

### Deel 2
#### State Space
De state space wordt berekend door het volgende:

```
Formule ((s*n)^rpt/rtts)
```

Nationaal
<br>Totaal aantal stations(s):                       64
<br>Minimale reistijd tussen twee stations(n):       5
<br>Maximaal aantal buren voor een station(rtts):    9
<br>Maximale reistijd per traject(rpt):              180
<br>Maximaal aantal trajects:                        20

```
((64*9)^(180/5))^n
= ((64*9)^36) + ((64*9)^36)^2 + ((64*9)^36)^3 + ...... ((64*9)^36)^20
= 5.50 e^716
```


#### Score Lower- en Upperbound
Respectievelijk de Lower en Upper bound voor 2d:
```
K: p = 1; T = 20; Min = 20*180 = 9240,0     K: p = 1; T = 6; Min = 1011; = 9778,9
```
Respectievelijk de Lower en Upper bound voor 2e:
```
K: p = 1; T = 20; Min = 20*180 = 9240,0     K: p = 1; T = 9; Min = 1551; = 9664.9
```

### Pijnpunten

- Utrecht Centraal heeft veel buren en zorgt voor een grote nStatespace
- De volgorde van je trajecten maakt heel erg uit en kan ervoor zorgen dat je uiteindelijk enkele kritieke sporen hebt die ver uit elkaar liggen


### Vereisten

Deze codebase is volledig geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:
```
pip install -r requirements.txt
```

### Structuur

Alle Python scripts met functies staan in de map Code, met daarin een map 'test' voor alle functies die we willen
testen. In de map Data zitten alle csv's die we importeren. In de algemene map zitten onze individuele Python scripts om de code te runnen.

### Test

Om de code te draaien voor onze algoritmes gebruik één van de volgende instructies:

Depth First met Random Selector:
```
  - python main.py region depth_first_random all_critical n_best n_iterations
```
waar region of Holland of Nationaal is, all_critical is een boolean, n_best
en n_interations zijn integers. Als dit gerund wordt zonder argumenten na 
depth_first_random worden de standaardinstellingen gebruikt. Als region
Nationaal is kan de runtime erg groot zijn, dus kijk daarmee uit.

Depth First met Look Ahead:
```
  python main.py region depth_first_look_ahead all_critical n_best
```
waar region of Holland of Nationaal is, all_critical is een boolean, n_best
is een integer. Als dit gerund wordt zonder argumenten na 
depth_first_look_ahead worden de standaardinstellingen gebruikt. Als region
Nationaal is kan de runtime erg groot zijn, dus kijk daarmee uit.

Draw best solution routes (depth first met look ahead):
```
  python main.py region draw_routes
```
where region is Nationaal

Hillclimber:
```
  python main.py region draw_hillclimber
```
where region is Nationaal

simulated annealingr:
```
  python main.py region draw_simulated
```
where region is Nationaal

### Keuzes

- In starts2.py hebben we ervoor gekozen om te beginnen bij vooral 'uitstekende'
stations. Hier moet je namelijk sowieso overheen, en als je er begint ga je maar
1 keer over de verbinding ipv 2. Verder hebben we ervoor gekozen om van deze
stations de stations met langere verbindingen boven de kortere te verkiezen,
zodat je latere trajecten minder in de weg zit.

- In depth_first_n_best.py hebben we ervoor gekozen om enkele heuristieken toe
te passen waardoor de runtime sterk verminderd wordt. Zo mag een traject maar
maximaal 2 keer over één station, en mag een traject alleen station A, B, A
kiezen als spoor AB kritiek is. Verder moet het eerste spoor in een traject
kritiek zijn. Ook wordt een route die begint bij Maastricht gedwongen om 
naar Heerlen heen en weer te gaan. Hierdoor hoef jemaar 1 keer over de rest
van Limburg te rijden en is de k-score vrijwel altijd hoger.

## Auteurs

- David Arisz
- Kennet Botan
- Timo Koster

## Dankwoord
- Okke
- Stack Overflow
- Minor programmeren van de UvA
