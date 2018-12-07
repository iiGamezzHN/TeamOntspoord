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
