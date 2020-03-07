board = []

class positionType:
    x = -1
    y = -1

def createBoard():
    rowBoard = []
    for i in range(0, 20):
        for j in range(0, 20):
            rowBoard.append(' ')
        board.append(rowBoard)
        rowBoard = []
    
def display_board():
    for i in range(0, len(board)):
        strRow = ''
        for j in range(0, len(board[i])):
            strRow += board[i][j] + " | "
        print(strRow)

def play_game():
    createBoard()
    # display_board()
    endGame = False
    xTurn = True
    position = positionType()
    player = 'x'

    while (not(endGame)):
        if (xTurn):
            player = 'x'
            position = choose_position('x')
        else:
            player = 'o'
            position = choose_position('o')
        xTurn = not(xTurn)
        
        print("-------------------------------------------------------")
        display_board()
        if (check_winning(player, position)):
            print(player + " are the winner")
            endGame = True
            

def choose_position(player):
    position = positionType()
    inputDone = False
    while (not(inputDone)):
        position.x = input("Choose position in row: ")
        position.y = input("Choose position in column: ")
        if (position.x >= 1 and position.x <= len(board) and position.y >= 1 and position.y <= len(board)):
            if (board[position.x - 1][position.y - 1] == ' '):
                board[position.x - 1][position.y - 1] = player
                inputDone = True

    position.x = position.x - 1
    position.y = position.y - 1
    return position

def check_winning(player, position):
    counterColumn = 0
    counterRow = 0
    counterCrossLeft = 0
    counterCrossRight = 0
    for i in range(-4, 5):
        #check horizontal
        if (position.y + i >= 0):
            if (board[position.x][position.y + i] == player):
                counterRow += 1
                if (counterRow == 5):
                    return True
            else:
                counterRow = 0
        #check vertical
        if (position.x + i >= 0):
            if (board[position.x + i][position.y] == player):
                counterColumn += 1
                if (counterColumn == 5):
                    return True
            else:
                counterColumn = 0
        #check crossLeft
        if (position.x + i >= 0 and position.y + i >= 0):
            if (board[position.x + i][position.y + i] == player):
                counterCrossLeft += 1
                if (counterCrossLeft == 5):
                    return True
            else:
                counterCrossLeft = 0
        #check crossRight
        if (position.x + i >= 0 and position.y - i >= 0):
            if (board[position.x + i][position.y - i] == player):
                counterCrossRight += 1
                if (counterCrossRight == 5):
                    return True
            else:
                counterCrossRight = 0
    return False

def inRange(position):
    if (position >= 0 and position <= 2):
        return True
    return False

if __name__== "__main__":
    play_game()