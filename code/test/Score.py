# p = 1
# T = [x for x in range(8)[1:]]
# Min = [x for x in range(121)[1:]]
#
# scores = []
#
# for y in T:
#     for z in Min:
#         scores.append(p * 10000 - (y * 20 + z / 10))
#
# #formule = p * 10000 - (T * 20 + Min / 10)
#
# print(max(scores))

from random import *
from math import *

times = {}

for x in range(10000):
    p = randint(1, 20)/20  # Fractie van bereden kritieke verbindingen
    T = randint(1, 7)  # Aantal trajecten
    Min_list = sample(range(20, 120), T) # Aantal min van trajecten
    Min = sum(Min_list) # Totale aantal min van trajecten
    value = p * 10000 - (T * 20 + Min / 10)
    times[value] = {'p':p,'T':T,'Min_list':Min_list,'Min':Min}

T = ceil(206/120)
print("Max score "+str(10000 - (T*20 + 206/10)))
print("Nr trajecten "+str(287/120))
print("Min score "+str(10000 - (7*20 + 7*120/10)))

# test = [('bla','la'),('tihi','hihi'),("bla",'tihi')]
#
# sum(x.count('bla') for x in test)
# asdf = 0
