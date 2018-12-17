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
```
Depth First met Random Selector:
  - python main.py depth_first_random region all_critical n_best n_iterations
  where region is either Nationaal or Holland, all_critical is a boolean,
  n_best and n_iterations are integers. If depth_first_random is run without
  any other aruments it will run in its default setting. If region is set to
  Nationaal runtime can be very long, so watch out for that.

Depth First met Look Ahead:
  python main.py depth_first_random region all_critical n_best
  where region is either Nationaal or Holland, all_critical is a boolean,
  n_best is an integers. If depth_first_random is run without
  any other aruments it will run in its default setting. If region is set to
  Nationaal runtime can be very long, so watch out for that.
```

## Auteurs

- David Arisz
- Kennet Botan
- Timo Koster

## Dankwoord
- Okke
- Stack Overflow
- Minor programmeren van de UvA
