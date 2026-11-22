# Tic Tac Toe

### Python-Based Two-Player Game

## Project Overview

Tic Tac Toe is a console-based, two-player game developed using Python. The game is played on a 3 × 3 board, where players take turns marking empty positions with their respective symbols, X and O.

The objective is to form a straight line of three identical symbols horizontally, vertically, or diagonally before the opponent.

## Game Rules

1. **Players:** The game supports two players. Player 1 uses X, and Player 2 uses O.

2. **Turn-Based Play:** Players take turns placing their symbols on the board. Player 1 always starts the game.

3. **Board Positions:** The board contains nine positions arranged in three rows and three columns. Players enter the row and column numbers, each ranging from 1 to 3.

4. **Valid Moves:** A player can place their symbol only in an empty position. Selecting an occupied position does not change the board or the current player's turn.

5. **Input Validation:** Empty inputs, non-numeric inputs, and positions outside the range of 1–3 are rejected. The player must enter a valid position to proceed.

6. **Winning Condition:** A player wins by placing three identical symbols in a horizontal, vertical, or diagonal line.

7. **Draw Condition:** If all nine positions are occupied and neither player has achieved a winning combination, the match ends in a draw.

8. **Match Completion:** The game ends when a player wins or the board is completely filled without a winner.

9. **Replay:** After each match, players can choose to play again. A new match starts with an empty board and Player 1's turn.

10. **Score Tracking:** The game maintains separate scores for Player 1, Player 2, and draws. Scores are updated after every completed match and displayed on the scoreboard.

## Winning Combinations

A player wins when their symbol occupies any one of the following eight combinations:

| Combination | Positions |
|---|---|
| Horizontal | Three rows |
| Vertical | Three columns |
| Diagonal | Top-left to bottom-right |
| Diagonal | Top-right to bottom-left |

## Game Flow

1. Initialize the board and scoreboard.
2. Display the board and identify the current player.
3. Accept row and column inputs.
4. Validate the selected position.
5. Place the player's symbol on the board.
6. Check for a winning combination.
7. Check for a draw if no winner is found.
8. Switch the player if the match continues.
9. Update and display the scoreboard after the match.
10. Ask whether the players want to play again.

## Project Structure

```text
Project/
│
├── tic_tac_toe.py
└── README.md
```

The main game logic is implemented in `tic_tac_toe.py`.

## Technologies Used

- Python 3
- Lists for board representation
- Functions for game logic and modularity
- Conditional statements and loops for turn management
- Input validation using exception handling

## Project Information

**Project Type:** College Project

**Category:** Python Console-Based Game

**Game:** Tic Tac Toe

