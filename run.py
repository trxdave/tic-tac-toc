import random

def printBoard():
    """ 
    Print the tic-tac-toe board
    """
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print('-+-+-')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('-+-+-')
    print(f'{board[0]} | {board[1]} | {board[2]}')

def gameover():
    """
    Gameover who is winner
    """
    # Check rows
    for i in range(0, 3 * 3, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    # Check if there is no winner
    if " " not in board:
        return "draw"

    return False

board = [" " for i in range(3 * 3)]

while True:
    x_to_play = True
    # X plays first
    print_board()
    out_of_moves = False
    someone_won = False

    while not out_of_moves and not someone_won:
        # Get player's move
        if x_to_play:
            player = "X"
            turn_message = "Player X's turn"
            computer = "O"
        else:
            player = "O"
            turn_message = "Player O's turn"
            computer = "X"

        # Get input
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (1-9)"))
                if move < 1 or move > 9:
                    raise ValueError
                if board[move - 1] == " ":
                    break

                print("That cell is already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 9")
        # Update the board
        board[move - 1] = player
        # Print the board
        print_board(board)

        # Check if the game is over
        if gameover(board) is not False:
            if x_to_play:
                print(f"{player} wins!")
            else:
                print(f"{computer} wins!")

            someone_won = True
            out_of_moves = True

        # Check if there are any moves left
        if not " " in board:
            print("Draw!")
            out_of_moves = True

        # Change turns
        x_to_play = not x_to_play

    if input("Do you want to play again (y/n): ").lower() == 'y':
    board = [" " for i in range(3 * 3)]
else:
    break
