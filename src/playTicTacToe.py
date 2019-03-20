board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

stateSequence = [board]

# currentPlayer stores the symbol corresponding to the current player's move
currentPlayer = 'X'

def checkNewBoardValidity(newBoard):
    boardFlat = [cell for cell in row for row in board]
    newBoardFlat = [cell for cell in row for row in newBoard]

    flatBoards = zip(boardFlat, newBoardFlat)

    differences = [positionValues for positionValues in flatBoards if positionValues[0] is not positionValues[1]]

    if len(differences) == 1:
        if differences[0][0] == ' ' and differences[0][1] == currentPlayer:
            return True
    
    return False

def updateBoard(newBoard):
    if checkNewBoardValidity(newBoard):
        board = newBoard
        stateSequence.append(board)

def getBoardState():
    return board

