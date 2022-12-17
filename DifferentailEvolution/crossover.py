from random import randint

import numpy as np

"""
@author: Maya
"""


def crossover(p1,p2):
    child = np.zeros((9, 9), dtype=np.int64)
    n = randint(1, 2)
    for y in range(9):
        if n == 1:
          child[y] = p1[randint(0, 8)]
        else:
          child[y] = p2[randint(0, 8)]
        n = randint(1, 2)
    return child

