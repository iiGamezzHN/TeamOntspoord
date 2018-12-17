import numpy as np
import matplotlib.pyplot as plt

objects = (3, 4, 5)
y_pos = np.arange(len(objects))
performance = [8592.9, 9597.6, 9631.3]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Score')
plt.xlabel('Depth')
plt.ylim([8500, 10000])
plt.title('Scores for n depth in Nationaal not critical')

plt.show()
