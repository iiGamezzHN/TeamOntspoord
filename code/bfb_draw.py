import numpy as np
import matplotlib.pyplot as plt


# Personally change ylim for good picture
def draw(objects, values):
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Score')
    plt.xlabel('Depth')
    plt.ylim([8500, 10000])
    plt.title('Scores for n depth in Nationaal not critical')

    plt.show()
