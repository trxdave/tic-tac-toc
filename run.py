import random
import curses
import os

def clear_screen():
    """
    Clean up the console.
    """
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    """
    Give a message for the player
    """
    print("Welcome to Tic Tac Toe!")
    print("Classic game where two players take turns marking spaces in a 3x3 grid.")
    print("The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.")
    print("You will be playing against the computer, which will be represented by '😠'. You will be '❌'.")
    print("To make your move, simply enter a number from 1 to 9 corresponding to the position you want to mark on the board, as shown below:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Get ready to enjoy the game!\n")
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            print(f"Hello, {name}!")
            return name
        else:
            print(f"{name} is invalid. Please enter a valid name")

def print_board(board, player):
    """
    Print the Tic Tac Toe board.
    """
    clear_screen()
    print(f"You are {player}\n")
    print("The First Player to get 3 in a row Wins!")
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_gameover(board):
    """
    Check if the game is over and who the winner is.
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

def computer_move(board):
    """
    Computer's move.
    """
    # Check if computer can win
    for i in range(3 * 3):
        if board[i] == " ":
            board[i] = "😠"
            if check_gameover(board) == "😠":
                return
            board[i] = " "

    # Check if player can win
    for i in range(3 * 3):
        if board[i] == " ":
            board[i] = "❌"
            if check_gameover(board) == "❌":
                return
            board[i] = " "

    # Choose a random empty cell
    while True:
        move = random.randrange(0, 3 * 3, 1)
        if board[move] == " ":
            board[move] = "😠"
            return

def main():
    """
    Main game loop.
    """
    player_name = get_player_name()
    player = "❌"
    computer = "😠"
    x_to_play = True
    board = [" " for i in range(3 * 3)]

    while True:
        print_welcome_message()
        while True:
            print_board(board, player)
            if x_to_play:
                valid_input = False
                while not valid_input:
                    try:
                        move = int(input(f"{player_name}'s turn (Enter a number from 1 to 9): "))
                        if 1 <= move <= 9:
                            if board[move - 1] == " ":
                                valid_input = True
                                board[move - 1] = player
                                break
                            else:
                                print("That cell is already occupied. Try again.")
                        else:
                            print("Invalid input. Please enter a number from 1 to 9.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print("Computer is thinking...")
                computer_move(board)

            if gameover_status := check_gameover(board):
                if gameover_status:
                    print_board(board, player)
                    print(f"{player} wins!")
                else:
                    print_board(board, player)
                    print("Draw!")
                break

            x_to_play = not x_to_play

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()
