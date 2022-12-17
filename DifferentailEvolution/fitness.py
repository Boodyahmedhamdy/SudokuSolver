import numpy as np

OPTIMAL_SUM = 45


def getIndividualFitness(individual):
    sumRowsList = calculateSumRows(individual)
    sumColumnsList = calculateSumColumns(individual)
    sumBlocksList = calculateSumBlocks(individual)

    rowsFitness = getListFitness(sumRowsList)
    columnsFitness = getListFitness(sumColumnsList)
    blocksFitness = getListFitness(sumBlocksList)

    fitness = rowsFitness + columnsFitness + blocksFitness

    return fitness


# returns 0 if passed list is fit
def getListFitness(list):
    fitness = 0
    for i in range(9):
        difference = abs(OPTIMAL_SUM - list[i][1])
        fitness += difference

    return fitness


def calculateSumColumns(individual):
    sumColumns = []
    for columnIndex in range(9):
        sumColumns.append(
            (columnIndex, calculateSumColumn(individual, columnIndex))
        )

    return sumColumns


def calculateSumColumn(individual, columnIndex):
    column = individual.T[columnIndex]
    # optimal is 45 -- from 1 to 9
    sumColumn = sum(set(column))

    return sumColumn


def calculateSumRows(individual):

    sumRows = []
    for rowIndex,  row in enumerate(individual):
        sumRows.append(
            (rowIndex, calculateSumRow(individual, rowIndex))
        )

    return sumRows


def calculateSumRow(individual, rowIndex):

    row = individual[rowIndex]

    # the optimal is 45 -- from 1 to 9
    sumRow = sum(set(row))

    return sumRow


def calculateSumBlocks(individual):
    """
    to calculate summition of all blocks in passed individual
    :param individual:
    :return: list of tuples [(block index, sum block)]
    """


    sumBlocks = []
    blockIndex = 0

    for rowIndex in range(0, 9, 3):
        for columnIndex in range(0, 9, 3):

            block = set()
            for i in range(3):
                for j in range(3):
                    block.add(individual[rowIndex + i][columnIndex + j])

            sumBlock = sum(block)
            sumBlocks.append((blockIndex, sumBlock))
            blockIndex += 1

    return sumBlocks


board = np.array(

    # bad board
    # [[1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [4, 5, 6, 4, 7, 4, 1, 9, 9],
    #  [7, 8, 9, 6, 6, 2, 2, 3, 6],
    #  [3, 4, 6, 7, 6, 3, 6, 2, 7],
    #  [2, 3, 7, 3, 6, 5, 2, 2, 1],
    #  [8, 9, 4, 4, 6, 9, 1, 5, 9],
    #  [9, 2, 8, 1, 6, 7, 9, 6, 5],
    #  [6, 6, 5, 5, 9, 4, 3, 4, 4],
    #  [5, 7, 1, 8, 9, 6, 7, 9, 9]]

    # right board
    [[2, 4, 1, 5, 6, 3, 7, 9, 8],
     [8, 5, 9, 1, 2, 7, 3, 6, 4],
     [7, 3, 6, 4, 8, 9, 1, 5, 2],
     [3, 6, 5, 7, 9, 2, 8, 4, 1],
     [1, 9, 2, 8, 4, 5, 6, 3, 7],
     [4, 7, 8, 3, 1, 6, 9, 2, 5],
     [6, 1, 4, 2, 3, 8, 5, 7, 9],
     [9, 8, 7, 6, 5, 4, 2, 1, 3],
     [5, 2, 3, 9, 7, 1, 4, 8, 6]]
)
print(board.T)

print(calculateSumRows(board))
print(calculateSumRows(board))
print(calculateSumBlocks(board))
print(getIndividualFitness(board))


