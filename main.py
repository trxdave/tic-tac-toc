print ("Welcome to Tic Tac Toe")
print ("Here is the board layout:")


def printBoard():
    """ 
    Board is a list of 10 strings representing the board 
    """
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def gameover():
    """
    Gameover who is winner
    """
    return (board[0] == board[1] == board[2] != " ") or (board[3] == board[4] == board[5] != " ")
    or (board[6] == board[7] == board[8] != " ") or (board[0] == board[4] == board[8] != " ")
    or (board[2] == board[4] == board[6] != " ") or (board[0] == board[3] == board [6] != " ")
    or (board[1] == board[4] == board[7] != " ") or (board[2] == board[5] == board [8] != " ")

def playerLetter():
    """
    The player pick which letter they want to be and computer's letter as the second.
    """
    player = ''
    while not (player == 'X' or player == 'O'):
        print("Do you want to be X or O?")
        player = input() .upper()

    if player == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    """
    Choose which player goes first.
    """
    if random.pick(0, 1) == 0:
        return 'computer'
    else:
        return 'player'



    