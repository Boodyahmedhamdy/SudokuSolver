import numpy as np
import random


mainBoard = np.array(
    [[1, 9, 3, 9, 3, 8, 9, 9, 6],
     [6, 7, 4, 4, 7, 4, 1, 9, 9],
     [1, 3, 2, 6, 6, 2, 2, 3, 6],
     [4, 4, 6, 7, 6, 3, 6, 2, 7],
     [2, 3, 7, 3, 6, 5, 2, 2, 1],
     [8, 9, 4, 4, 6, 9, 1, 5, 9],
     [7, 2, 8, 1, 6, 7, 9, 6, 5],
     [1, 6, 5, 5, 9, 4, 3, 4, 4],
     [7, 7, 1, 8, 9, 6, 7, 9, 9]]
)



def mutatePopulation(population, mutationRate = 0.2):

    pass

def mutateIndividual(individual, numberOfMutaitons = 3):

    betterIndividual = individual

    for _ in range(numberOfMutaitons):
        randomIndex = random.randint(0, 8)
        swapRow(betterIndividual, randomIndex)
        swapColumn(betterIndividual, randomIndex)

    return betterIndividual


def swapRow(board, rowIndex):
    row = board[rowIndex]

    firstRandomIndex = random.randint(1, 9)
    secondRandomIndex = random.randint(1, 9)

    row[firstRandomIndex], row[secondRandomIndex] =\
        row[secondRandomIndex], row[firstRandomIndex]


def swapColumn(board, columnIndex):

    column = board.T[columnIndex]

    firstRandomIndex = random.randint(1, 9)
    secondRandomIndex = random.randint(1, 9)

    column[firstRandomIndex], column[secondRandomIndex] = \
        column[secondRandomIndex], column[firstRandomIndex]


print(mainBoard)
swapRow(mainBoard, 0)
print("-------swapped the row---------")
print(mainBoard)
print("-------swapped the column---------")
swapColumn(mainBoard, 1)
print(mainBoard)
print("----------------")


# mainBoard = mutateIndividual(mainBoard)
# print(mainBoard)

