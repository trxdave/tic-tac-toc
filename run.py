"""
Tic Tac Toe Game

This module implements a simple Tic Tac Toe game where a player competes
against the computer.
"""

import random
import os
import colorama
from colorama import Fore

colorama.init()


def clear_screen():
    """
    Clean up the mess
    """
    os.system("cls" if os.name == "nt" else "clear")


def intro():
    """
    Give a message for the player
    """
    print(Fore.GREEN + "WELCOME TO")
    print(r"""
  _____ _      _____          _____
 |_   _|_|__  |_   _|_ _ __  |_   _|__  ___
   | | | / _|   | |/ _` / _|   | |/ _ \/ -_/
   |_| |_\__|   |_|\__,_\__|   |_|\___/\___|
""")
    print(Fore.RESET)
    print(
        Fore.YELLOW + "Classic game where two players take turns marking "
        "spaces in a 3x3 grid.\n"
        "The player who succeeds in placing three of their marks in a "
        "horizontal, vertical, or diagonal row wins the game.\n"
        "You will be playing against the computer, which will be represented "
        "by '😠'. You will be '❌'.\n"
        "To make your move, simply enter a number from 1 to 9 corresponding "
        "to the position you want to mark on the board, as shown below:"
    )

    print(Fore.RESET)
    print(Fore.CYAN + " 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print(Fore.RESET)
    print(Fore.RED + "GAME RULES!")
    print(
        "The first player to get three of their marks in a row, column, or"
        "diagonal wins the game."
    )
    print(
        "If all the cells are filled without any player achieving three in a"
        "row, the game ends in a draw."
    )
    print(Fore.RESET)
    print("Get ready to enjoy the game!\n")
    while True:
        name = input(Fore.GREEN + "Please enter your name: ").strip()
        if name.isalpha():
            return name
        else:
            print(Fore.RED + f"{name} is invalid. Please enter a valid name")
            print(Fore.RESET)


def print_board(board, player):
    """
    Print the Tic Tac Toe board.
    """
    clear_screen()
    print(Fore.GREEN + f"You are {player}\n")
    print("Current Board:")
    print("The First Player to get 3 in a row Wins!")
    print(Fore.RESET)
    print(Fore.CYAN + f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print(Fore.RESET)


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

            # Reset the move if it doesn't lead to a win
            board[i] = " "

    # Check if player can win and block them
    for i in range(3 * 3):
        if board[i] == " ":
            board[i] = "❌"
            if check_gameover(board) == "❌":
                board[i] = "😠"
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
    while True:
        clear_screen()
        player_name = intro()
        print("Player name:", player_name)
        player = "❌"
        computer = "😠"
        x_to_play = True
        board = [" " for i in range(3 * 3)]

        while True:
            while True:
                print_board(board, player)
                if x_to_play:
                    valid_input = False
                    while not valid_input:
                        try:
                            move = int(input(
                             f"{player_name}'s turn (Enter a number from 1-9):"
                            ))
                            if 1 <= move <= 9:
                                if board[move - 1] == " ":
                                    valid_input = True
                                    board[move - 1] = player
                                    break
                                else:
                                    print(
                                        Fore.RED + "That cell is already"
                                        "occupied. Try again."
                                    )
                            else:
                                print(
                                    "Invalid input. Please enter a number from"
                                    "1 to 9."
                                )
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            print(Fore.RESET)
                else:
                    print("Computer is thinking...")
                    computer_move(board)

                if gameover_status := check_gameover(board):
                    if gameover_status == "❌":
                        print_board(board, player)
                        print(Fore.GREEN + f"{player} wins!")
                    elif gameover_status == "😠":
                        print_board(board, player)
                        print(f"{computer} wins")
                        print(Fore.RESET)
                    else:
                        print_board(board, player)
                        print(Fore.YELLOW + "Draw!")
                    break

                x_to_play = not x_to_play

            play_again = input("Do you want to play again? (y/n): ") \
                .strip() \
                .lower()
            if play_again != "y":
                print(r"""
 _  _                                           _                 _
| || |___ _ __  ___   _  _ ___ _  _   ___ _ _  |_|___ _  _ ___ __| |
| __ / _ \ '_ \/ -_\ | || / _ \ || | / -_\ ' \ | / _ \ || / -_\ _` |
|_||_\___/ .__/\___|  \_, \___/\_,_| \___|_||_|/ \___/\_, \___\__,_|
 _____ _ |_|  _____   |__/   _____         _ |__/     |__/
|_   _|_|__  |_   _|_ _ __  |_   _|__  ___| |
  | | | / _|   | |/ _` / _|   | |/ _ \/ -_\_|
  |_| |_\__|   |_|\__,_\__|   |_|\___/\___|_|
""")
                print(Fore.RESET)
                return
            else:
                board = [" " for i in range(3 * 3)]
                x_to_play = True


if __name__ == "__main__":
    main()
