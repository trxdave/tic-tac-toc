import random
import curses
import os

def clear():
    """
    Clean up the function of the mess.
    """
    os.system("cls" if os.name == "nt" else "clear")

def printing_Board(board, player):
    """
    Print the tic-tac-toe board
    """
    clear()
    print(f"You are {player}\n")
    print("The First Player to get 3 in a row Wins!")
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def gameover(board):
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

def computer_move(board):
    """
    Computer's move
    """
    # Check if computer can win
    for i in range(3 * 3):
        if board[i] == " ":
            board[i] = "😠"
            if gameover(board) == "😠":
                return
            board[i] = " "

    # Check if player can win
    for i in range(3 * 3):
        if board[i] == " ":
            board[i] = "❌"
            if gameover(board) == "❌":
                return
            board[i] = " "

    # Choose a random empty cell
    while True:
        move = random.randrange(0, 3 * 3, 1)
        if board[move] == " ":
            board[move] = "😠"
            return

def main(stdscr):
    """
    This is the main function of the Tic Tac Toe game.
    """
    while True:
        player_score = 0
        computer_score = 0
        name = intro()
        player = "❌"
        computer = "😠"
        x_to_play = True
        board = [" " for i in range(3 * 3)]
        printing_Board(board, player)
        out_of_moves = False
        someone_won = False

        while not out_of_moves and not someone_won:
            # Get player's move
            if x_to_play:
                turn_message = f"{name}'s turn"
            else:
                turn_message = "Computer's turn"

            # Get input
            if x_to_play:
                while True:
                    try:
                        move = int(input(f"{turn_message} (Enter a number from 1 to 9):"))
                        if move < 1 or move > 9:
                            print("Invalid input. Please enter a number from 1 to 9.")
                            continue
                        if board[move - 1] == " ":
                            break
                        else:
                            print("That cell is already occupied. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # Update the board
                board[move - 1] = player
            else:
                computer_move(board)

            # Redraw the board
            printing_Board(board, player)

            # Check if the game is over
            winner = gameover(board)
            if winner:
                if winner == player:
                    player_score += 1
                    print(f"{player} wins!")
                elif winner == "😠":
                    computer_score += 1
                    print(f"{computer} wins!")
                else:
                    print("Draw")
                someone_won = True
                out_of_moves = True

            # Check if there are any moves left
            if not " " in board:
                print("Draw!")
                out_of_moves = True

            # Change turns
            x_to_play = not x_to_play

        print(f"Scoreboard - {name}: {player_score} {computer}: {computer_score}")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    curses.wrapper(main)
