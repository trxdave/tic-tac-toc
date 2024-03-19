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
    return (board[7] == board[8] == board[9] != " ") or (board[4] == board[5] == board[6] != " ")
    or (board[1] == board[2] == board[3] != " ") or (board[7] == board[4] == board[1] != " ")
    or (board[8] == board[5] == board[2] != " ") or (board[9] == board[6] == board [3] != " ")
    or (board[7] == board[5] == board[3] != " ") or (board[9] == board[5] == board [1] != " ")

if gameover():
    if x_to_play:
        print("O wins!")
        someone_won = True
    if not(x_to_play):
        print("X wins!")
        someone_won = True
if out_of_moves and not(someone_won):
    print("Draw!")

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

while not (gameover()):
    if x_to_play:
        move = int(input("It's X's turn. Chose 1-9"))
        if move<10 and move>0:
            if board[move-1] == "X" or board[move-1] == "0":
                used_tile = True
                moves_done = moves_done - 1
            else:
                invalid_input = True
                moves_done = moves_done - 1
            else:
        move = int(input("It's O's turn. Choose 1-9 "))
        if move<10 and move>0:
        if board[move-1] == "X" or board[move-1] == "O":
          used_tile = True
          moves_done = moves_done - 1
            else:
                board[move-1] = "O"
            else:
                invalid_input = True
        moves_done = moves_done - 1
        if used_tile == False and invalid_input == False:
        x_to_play = not(x_to_play)
        os.system("clear")
        printboard()
        elif invalid_input == True:
        print("Invalid input! Try again.")
        invalid_input = False
            else:
                print("A player already chose this spot! Try again.")
                used_tile = False
        moves_done = moves_done + 1
        if moves_done == 9:
            out_of_moves = True
            break

def boardCopy (board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


    