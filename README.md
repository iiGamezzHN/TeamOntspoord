# TeamOntspoord - RailNL

Voor het project is gekozen voor het onderwerp RailNL, waarin een lijnvoering gemaakt moet worden voor de intercity treinen in
Nederland.

In deel 1 van de opdracht moet er er lijnvoering gemaakt worden voor Noord- en Zuid Holland.
De Scorefunctie is K = 10000 * p - (T*20 + Min/10). Hierbij is p de fractie van het aantal bereden kritieke trajecten, T het aantal gebruikte Tracks en Min het totaal aantal minuten van alle Tracks bij elkaar.

## Aan de slag
### Deel 1
#### State Space, Upper en Lower Bounds
De state space wordt berekend door het volgende:

#### Score
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
#### State Space, Upper en Lower Bounds
De state space wordt berekend door het volgende:

Formule ((s*n)^rpt/rtts)

Holland
Totaal aantal stations:                       22
Maximaal aantal buren voor een station:       4
Minimale reistijd tussen twee stations:       5
Maximale reistijd per traject:                120
Maximaal aantal trajects:                     7

```
((22*4)^(120/5))^n
= ((22*4)^24) + ((22*4)^24)^2 + ((22*4)^24)^3 + ...... + ((22*4)^24)^7
= 2.73 e^108
```

Nationaal
Totaal aantal stations:                       64
Maximaal aantal buren voor een station:       9
Minimale reistijd tussen twee stations:       5
Maximale reistijd per traject:                180
Maximaal aantal trajects:                     20

```
((64*9)^(180/5))^n
= ((64*9)^36) + ((64*9)^36)^2 + ((64*9)^36)^3 + ...... ((64*9)^36)^20
= 5.50 e^716
```


#### Score
Respectievelijk de Lower en Upper bound voor 2d:
```
K: p = 1; T = 20; Min = 7*180 = 9474.0     K: p = 1; T = 7; Min = 1239; = 9736.1
```
Respectievelijk de Lower en Upper bound voor 2e:
```
K: p = 1; T = 20; Min = 7*180 = 9474.0     K: p = 1; T = 9; Min = 1551; = 9664.9
```

### Pijnpunten

-Het hillclimberalgoritme moet nog erg lang rekenen voor heel Nederland
-


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
python mainTimo.py
python mainKennet.py
python mainDavid.py
```

## Auteurs

- David Arisz
- Kennet Botan
- Timo Koster

## Dankwoord
- Stack Overflow
- Minor programmeren van de UvA
