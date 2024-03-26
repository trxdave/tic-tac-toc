# Tic-Tac-Toe

## Introduction ##

Are you ready to engage in a classic battle of wits against the computer? Tic Tac Toe is a timeless game where two players take turns marking spaces in a 3x3 grid, aiming to be the first to align three of their marks horizontally, vertically, or diagonally.

In this digital rendition of the game, you'll be facing off against an AI opponent represented by '😠', while you'll be '❌'. The rules are simple: strategically place your mark in an empty cell by entering a number from 1 to 9, corresponding to the position on the board.

Here's a quick overview of the game rules:

The first player to get three of their marks in a row, column, or diagonal wins.
If all the cells are filled without any player achieving three in a row, the game ends in a draw.
Get ready to exercise your tactical prowess and enjoy the thrill of victory in this classic game of Tic Tac Toe!

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

 The Tic-Tac-Toe game begins by asking the player to choose between X or O, after which both the player and computer take turns making moves. 

![alt text](documents/flowchart/chart.png)

The flowcharts on the left demonstrate the series of events that occur during the player's turn, while the ones on the right represent what takes place during the computer's turn. Once the player or computer has made a move, the program checks whether they have won or caused a tie, and then switches turns. 
After the game is complete, the program prompts the player to decide whether they would like to play again.

https://medium.com/chat-gpt-now-writes-all-my-articles/creating-a-tic-tac-toe-game-in-python-859fbad07f30
