# Tic-Tac-Toe

## Introduction ##

Are you up for a game of Tic Tac Toe against a computer? It's a timeless game where two players take turns marking spaces in a 3x3 grid. The objective is to be the first to align three of your marks horizontally, vertically, or diagonally.

In this digital version of the game, you'll be playing against an AI opponent represented by '😠', while you'll be '❌'. To play, you just need to strategically place your mark in an empty cell by entering a number from 1 to 9, corresponding to the position on the board.

Here are the game rules:

- The first player to get three of their marks in a row, column, or diagonal wins.
- If all the cells are filled without any player achieving three in a row, the game ends in a draw.

Get ready to exercise your tactical skills and experience the thrill of victory in this classic game of Tic Tac Toe!

## Live Project ##

## Design ##

### Colours ###

Green: Used for the welcome message and player prompts.
Yellow: Used for game instructions and important information about the game.
Cyan: Used for displaying the Tic Tac Toe board and numerical grid positions.
Red: Used for error messages or warnings.
Reset: Used to reset the color back to default after displaying colored text.

These colors are implemented using the Colorama library in Python, which allows for easy cross-platform colored text output in the console. You can customize the colors or add more as per your preference by modifying the code.

https://www.youtube.com/watch?v=u51Zjlnui4Y
https://pypi.org/project/colorama/

### Emoji ###

The Tic Tac Toe Emojis package provides emojis for the game and allows them to be applied to text in the terminal.
https://emojidb.org/tic-tac-toe-emojis

## Flowchart ##

![alt text](documents/flowchart/chart.png)

Start: The program starts here.
Initialize Game: Necessary variables are initialized, such as the game board, player markers, and screen-clearing function.
Display Introduction: The game introduces itself and provides instructions to the player.
Get Player Name: Prompt the player to enter their name.
Game Loop Begins: Enter the main game loop.
Display Board: Show the current state of the game board.
Player Turn: Prompt the current player to make a move.
Check Validity of Move: Ensure the move is valid (i.e., the selected cell is empty).
Update Board: If the move is valid, update the board with the player's marker.
Check for Win/Draw: Check if the game has been won or if it's a draw.
If a win or draw is detected, proceed to the appropriate end game state.
Switch Players: Switch to the next player's turn.
End Game States:
Win: Display the winning player and ask if they want to play again.
Draw: Notify the players that the game ended in a draw and ask if they want to play again.
Play Again?:
If the players choose to play again, reset the game and return to the start of the game loop.
If the players choose not to play again, end the program.

https://medium.com/chat-gpt-now-writes-all-my-articles/creating-a-tic-tac-toe-game-in-python-859fbad07f30
