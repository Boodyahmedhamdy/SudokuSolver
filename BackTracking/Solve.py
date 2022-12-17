import numpy as np
import random

# creating empty board
def createEmptyBoard():
    """
    to create empty board to fill it later with another function

    :return: empty 2D numpy array
    """

    board = np.array([
        np.zeros(9, dtype=int) for _ in range(9)
    ])
    return board


# create initial board
def createBoard(cellsNumberToBeFilled = 17):
    """

    :param cellsNumberToBeFilled: number of cells to be filled with random numbers as a start -- default 17
    :return: 2D numpy array with random values
    """

    board = createEmptyBoard()

    while cellsNumberToBeFilled > 0:
        randomNumber = random.randint(1, 9)
        randomRowIndex = random.randint(0, 8)
        randomColumnIndex = random.randint(0, 8)

        if isAvailableToAddNumberInBoard(board, randomNumber,
                                         randomRowIndex, randomColumnIndex):

            board[randomRowIndex][randomColumnIndex] = randomNumber
            cellsNumberToBeFilled -= 1

    return board


# board check
def isAvailableToAddNumberInBoard(board, number, rowIndex, columnIndex):
    """

    :param board: board to check availability on       
    :param number: number you would add
    :param rowIndex: row index to add the number in
    :param columnIndex: column index to add the number in
    :return: True if possible otherwise False
    """
    # check rows
    availableRow = isAvailableToAddNumberInRow(board, number, rowIndex)

    # check columns
    availableColumn = isAvailableToAddNumberInColumn(board, number, columnIndex)

    # check blocks
    availableBlock = isAvailableToAddNumberInBlock(board, number, rowIndex, columnIndex)

    if availableRow and availableColumn and availableBlock:
        return True

    return False


# row check
def isAvailableToAddNumberInRow(board, number, rowIndex):
    """

    :param board: board to check the availability on
    :param number: number you would add
    :param rowIndex: row index to add the number in
    :return: boolean -> True if possible otherwise False
    """
    if number not in board[rowIndex]:
        return True

    return False


# column check
def isAvailableToAddNumberInColumn(board, number, columnIndex):
    """

    checks if it is right to add number in given column or not

    :param board: the board that you want to check availability on
    :param number: number you would add
    :param columnIndex: column index to add the number in
    :return: boolean -> True if available to add the number otherwise False
    """
    if number not in board.T[columnIndex]:
        return True

    return False


# block check
def isAvailableToAddNumberInBlock(board, number, rowIndex, columnIndex):
    """

    :param board: board to check the availability in
    :param number: number you would add
    :param rowIndex: row index to add the number in
    :param columnIndex: column index to add the number in
    :return: boolean -> True it is possible to add the number otherwise False
    """

    row0 =(rowIndex//3)*3
    column0 =(columnIndex //3)*3

    for r in range(3):
        for c in range(3):
            if board[row0 + r][column0 + c] == number:
                return False

    return True


def getSavedPositions(board):
    """

    :param board: must be the initial board
    :return: set of saved positions which means all another
    """
    savedPositions = set()

    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                savedPositions.add((row, col))

    return savedPositions

# printing the board
def printBoard(board):
    """
    :param board: 2d numpy array to represent the sudoku board
    :param emptySymbol: what to put in empty cells instead of zero -- default *
    """
    print("\n-------------------------")

    for i in range(9):
        for j in range(9):
            if board[i][j] is not None:
                if j == 0:
                    print("|", end=" ")
                print(f"{board[i][j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end=" ")
        print()


def findNextEmpty(board):
    """
    find the empty squares 
    :param board: 2d numpy array to represent the sudoku board
    :return: the position of the empty squares if there is else None, None
    """
    for rowIndex in range(9):
        for columnIndex in range(9):
            if board[rowIndex][columnIndex] == 0:
                return rowIndex, columnIndex
            
    return None, None

def solveBoard(board):
    """
    solve the board 
    :param board: 2d numpy array to represent the sudoku board
    :return: solved Sudoku board
    """
    rowIndex, columnIndex = findNextEmpty(board)
    
    if rowIndex is None:
        return True
    
    for number in range(1, 10):
        if isAvailableToAddNumberInBoard(board, number, rowIndex, columnIndex):
            board[rowIndex][columnIndex] = number
            if solveBoard(board):
                return True
        board[rowIndex][columnIndex] = 0 
    
    return False      


# Test
if __name__=='__main__':
    board = createBoard()
    printBoard(board)
    solveBoard(board)
    printBoard(board)