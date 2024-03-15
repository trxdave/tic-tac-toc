
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def playerLetter():
    player = ''
    while not (player == 'X' or player == 'O'):
        print("Do you want to be X or O?")
        player = input() .upper()

    if player == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'



def makeMove():

def winner():

def getPlayerMove():

def getComputerMove():

    