from random import randint
import numpy as np
from createBoard import getSavedPositions, createBoard

"""
population creation phase

@author: Maya Ahmed

"""

def createPopulation(numberofpopulation=10):

    pop = np.zeros((numberofpopulation,9, 9), dtype=np.int64)
    for z in range(numberofpopulation):
        for x in range(9):
            for y in range(9):
                if (x, y) not in savedPositions:
                    pop[z][x][y] = randint(1, 9)
                else:
                    pop[z][x][y] = grid[x][y]

    return pop

# For testing only
def createPopulationFromBoard(board, numberofpopulation=10):

    pop = np.zeros((numberofpopulation, 9, 9), dtype=np.int64)
    savedPositions = getSavedPositions(board)

    for z in range(numberofpopulation):
        for x in range(9):
            for y in range(9):
                if (x, y) not in savedPositions:
                    pop[z][x][y] = randint(1, 9)
                else:
                    pop[z][x][y] = board[x][y]

    return pop

print("nothing")
board = createBoard()
pop = createPopulationFromBoard(board)

print(pop)

