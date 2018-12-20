import numpy as np
import matplotlib.pyplot as plt


# Personally change ylim for good picture
def draw(objects, val1, min):
    minimum = min-200

    plt.plot(objects, val1, 'o-')
    plt.xlabel('depth')
    plt.ylabel('Score')
    plt.ylim([minimum, 10000])
    plt.title('Scores for depth in Holland not critical')
    # plt.legend(['depth 3', 'depth 5', 'depth 7', 'depth 9'], loc='lower left')

    plt.show()

def draw2(objects, val1, min, val2, val3):
    minimum = min-200
    # x = np.array(objects)
    # y = np.array(values)
    plt.plot(objects, val1, 'o-')
    plt.plot(objects, val2, 'o-')
    plt.plot(objects, val3, 'o-')
    plt.xlabel('n_best')
    plt.ylabel('Score')
    plt.ylim([minimum, 10000])
    plt.title('Scores for n_best routes in Holland not critical')
    plt.legend(['depth 3', 'depth 5', 'depth 7', 'depth 9'], loc='lower left')
    plt.show()
