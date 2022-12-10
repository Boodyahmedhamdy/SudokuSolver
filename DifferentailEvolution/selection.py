import numpy as np

"""
@author: Maya
"""


def selectParents(population,fitness_vals):
    probs = fitness_vals.copy()
    probs += abs(probs.min()) + 1
    probs = probs/probs.sum()
    n = len(population)
    indcies = np.arange(n)
    selected_indices = np.random.choice(indcies, size=n, p=probs)
    selected_population = population[selected_indices]
    return selected_population

