from stateData import validStates
from adjacencyData import adjacentStates
from ast import literal_eval as make_tuple

board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '))

stateSequence = [board]

# currentPlayer stores the symbol corresponding to the current player's move
currentPlayer = 'X'


def checkNewBoardValidity(newBoard):
    return newBoard in adjacentStates[board]


def updateBoard(newBoard):
    if checkNewBoardValidity(newBoard):
        global board
        board = newBoard
        stateSequence.append(board)
    else:
        print("invalid move")


def getBoardState():
    return board


def printBoardState():
    for row in range(3):
        print('|', end='')
        for col in range(3):
            print(board[row][col], end='|')
        print('')


def isGameOver():
    return False


def play():
    printBoardState()

    while(not isGameOver()):
        #row, col = [int(num) for num in input('').split(' ')]
        newBoardState = make_tuple(input(''))
        updateBoard(newBoardState)
        printBoardState()


play()
