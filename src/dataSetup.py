import pprint

states = []

for s in range(0,3 ** 9):
    i = s
    cells = []
    for a in range(9,0,-1):
        if (i % 3 == 0):
            a = ' '
        elif (i % 3 == 1):
            a = 'O'
        else:
            a = 'X'
        cells = [a] + cells
        i = i // 3
    
    state = ((cells[0],cells[1],cells[2]), (cells[3],cells[4],cells[5]), (cells[6],cells[7],cells[8]))
    states.append(state)

validStates = []

for state in states:
    strate = ''.join(state[0]) + ''.join(state[1]) + ''.join(state[2])
    Ocount = strate.count('O')
    Xcount = strate.count('X')
    if abs(Ocount - Xcount) <= 1:
        validStates.append(state)


pp = pprint.PrettyPrinter(stream=open("stateData",'w'), indent=4)
pp.pprint(validStates)

def checkNewBoardValidity(board, newBoard):
    boardFlat = [board[i][j] for j in range(0,3) for i in range(0,3)]
    newBoardFlat = [newBoard[i][j] for j in range(0,3) for i in range(0,3)]

    flatBoards = zip(boardFlat, newBoardFlat)

    differences = [positionValues for positionValues in flatBoards if positionValues[0] is not positionValues[1]]

    if len(differences) == 1:
        if differences[0][0] == ' ':
            return True
    
    return False

adjacentStates = {}

for state1 in validStates:
    for state2 in validStates:
        if checkNewBoardValidity(state1, state2):

            if adjacentStates.get(state1) == None:
                adjacentStates[state1] = [state2]
            else:
                adjacentStates[state1].append(state2)

pp = pprint.PrettyPrinter(stream=open("adjacencyData.py",'w'))
pp.pprint(adjacentStates)
