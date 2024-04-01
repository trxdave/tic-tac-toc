# Tic-Tac-Toe

## Introduction ##

Are you up for a game of Tic Tac Toe against a computer? It's a timeless game where two players take turns marking spaces in a 3x3 grid. The objective is to be the first to align three of your marks horizontally, vertically, or diagonally.

In this digital version of the game, you'll be playing against an AI opponent represented by '😠', while you'll be '❌'. To play, you just need to strategically place your mark in an empty cell by entering a number from 1 to 9, corresponding to the position on the board.

Here are the game rules:

- The first player to get three of their marks in a row, column, or diagonal wins.
- If all the cells are filled without any player achieving three in a row, the game ends in a draw.

Get ready to exercise your tactical skills and experience the thrill of victory in this classic game of Tic Tac Toe!

## Live Project ##

[View Live Project Here]()

## Design ##

### Colours ###

- Green: Used for the welcome message and player prompts.
- Yellow: Used for game instructions and important information about the game.
- Cyan: Used for displaying the Tic Tac Toe board and numerical grid positions.
- Red: Used for error messages or warnings.
- Reset: Used to reset the color back to default after displaying colored text.

These colors are implemented using the Colorama library in Python, which allows for easy cross-platform colored text output in the console. You can customize the colors or add more as per your preference by modifying the code.

- [How to Print Colored Text in Python](https://www.youtube.com/watch?v=u51Zjlnui4Y)
- [colorma 0.4.6](https://pypi.org/project/colorama/)

### Emoji ###

The Tic Tac Toe Emojis package provides emojis for the game and allows them to be applied to text in the terminal.

[Emoji](https://emojidb.org/tic-tac-toe-emojis)

## Flowchart ##

![alt text](documents/flowchart/chart.png)

- Start: The program starts here.
- Initialize Game: Necessary variables are initialized, such as the game board, player markers, and screen-clearing function.
- Display Introduction: The game introduces itself and provides instructions to the player.
- Get Player Name: Prompt the player to enter their name.
- Game Loop Begins: Enter the main game loop.
- Display Board: Show the current state of the game board.
- Player Turn: Prompt the current player to make a move.
- Check Validity of Move: Ensure the move is valid (i.e., the selected cell is empty).
- Update Board: If the move is valid, update the board with the player's marker.
- Check for Win/Draw: Check if the game has been won or if it's a draw.
- If a win or draw is detected, proceed to the appropriate end game state.
- Switch Players: Switch to the next player's turn.
- End Game States:
- Win: Display the winning player and ask if they want to play again.
- Draw: Notify the players that the game ended in a draw and ask if they want to play again.
- Play Again?:
- If the players choose to play again, reset the game and return to the start of the game loop.
- If the players choose not to play again, end the program.

## Features ##

### Welcome Message and Introduction: ###

- Upon starting the game, the player is greeted with a stylish header and a brief introduction to the game's rules and mechanics.
- The system asks the user to provide their name and ensures that only alphabetic characters are accepted.

### Printing the Game Board: ###

- The 'print_board()' function displays the current state of the Tic Tac Toe game board to the player.
- It shows the positions on the board with numbers for player reference.

### Game Logic: ###

- The function checks the board state to determine the winner or if it's a draw and if the game is over. 
- It checks for winning conditions in rows, columns, and diagonals, as well as for a draw condition.

### Computer Move: ###

- This function is responsible for executing the logic that determines the computer player's move.
- After checking if the computer can win on its next move, if not, it blocks the player from winning, and if neither, it makes a random move.

### Main Game Loop ###

- The main() function is responsible for managing the game's flow.
- It prompts the player for their name, displays the introduction, and begins a new game repeatedly.
- Each game consists of alternating, player and computer turns until a win or draw.
- At the end of every game, the system prompts the player to ask if they would like to play again.

### Input Validation: ###

- It ensures that the player's input for their name and moves are valid.
- Name input only accepts alphabetic characters.
- Move input only accepts integers from 1 to 9 and checks if the chosen position is empty.

### Styling with Colorama: ###

- The colorama library is used for coloring the console output, enhancing the visual appeal of the game.
- Different colors are used for headers, prompts, and game status messages, making them more distinguishable and engaging.

# Technologies Used #

## Languages Used ##

* [Python](https://www.python.org/)

## Frameworks - Libraries - Programs Used ##

* GitHub as software hosting platform that enables users to store their projects in a remote location. This allows for easy access and collaboration on the project from different locations. [GitHub](https://www.github.com/)
* GitPod as developer hosting platform. [GitPod](https://www.gitpod.com)
* Heroku is a cloud platform as a service (PaaS) that allows developers to build, deploy, manage, and scale applications effortlessly. It provides a platform for hosting web applications, databases, and other software services, removing the need for developers to manage underlying infrastructure. [Heroku](https://id.heroku.com/login)
* A CI (Continuous Integration) Python linter is a tool used in the context of Continuous Integration pipelines to check Python code for adherence to coding standards, best practices, and potential errors or style issues. [CI Python Linter](https://pep8ci.herokuapp.com/)
* Logo fonts Tic Tac Toe and Hope you enjoyed Tic Tac Toe. [patorjk](https://patorjk.com/software/taag/#p=testall&f=Impossible&t=Tic%20tac%20toe)
* Lucidchart is a web-based diagramming tool used for creating flowcharts, mind maps, organizational charts, network diagrams, and other types of visual representations. 
 [LucidChart](https://www.lucidchart.com/pages/)
* In the context of Tic Tac Toe, emojis can be used to represent the players' moves on the game board instead of traditional X's and O's. Emojis add a fun and visually appealing element to the game, making it more engaging for players. [Emoji](https://emojidb.org/tic-tac-toe-emojis)
* It helps users improve the quality and correctness of their written communication by identifying grammatical errors, spelling mistakes, punctuation issues, and style inconsistencies in their text. [Grammarly](https://www.grammarly.com/)
* Start read the instructions on how to use Tic Tac Toe [Start read Tic Tac Toe](https://medium.com/chat-gpt-now-writes-all-my-articles/creating-a-tic-tac-toe-game-in-python-859fbad07f30)

# Validator Testing #

## CI Python Linter ##

* I used CI Python Linter (https://pep8ci.herokuapp.com) to remove all errors from the code. The code is now error-free and optimized for performance.

![alt text](<documents/testing/CI Python Linter.png>)
