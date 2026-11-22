
# =================================
#       TIC TAC TOE GAME
# =================================

def display_board(board):

    print("\n")
    print("       TIC TAC TOE")
    print("-----------------------")

    print(" ", board[0], "|", board[1], "|", board[2])
    print(" ---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print(" ---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])

    print("-----------------------")




def check_winner(board):

    win = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for i in win:

        if board[i[0]] == board[i[1]] == board[i[2]] == "X":
            return "X"

        if board[i[0]] == board[i[1]] == board[i[2]] == "O":
            return "O"

    return None



def play_game():

    board = [" "] * 9

    player = "X"

    while True:

        display_board(board)

        if player == "X":
            print("\nPlayer 1 - X turn")
        else:
            print("\nPlayer 2 - O turn")

       
        try:

            row = input("Enter row (1-3): ").strip()

            col = input("Enter column (1-3): ").strip()

            if row == "" or col == "":
                print("Input cannot be empty!")
                continue

            row = int(row)
            col = int(col)

            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid position! Enter between 1 and 3.")
                continue

        except ValueError:

            print("Please enter numbers only!")
            continue

        
        position = (row - 1) * 3 + (col - 1)

    
        if board[position] != " ":

            print("This position is already occupied!")
            continue

       
        board[position] = player

       
        winner = check_winner(board)

        if winner:

            display_board(board)

            if winner == "X":
                print("\nPlayer 1 (X) Wins!")
            else:
                print("\nPlayer 2 (O) Wins!")

            return winner

       
        if " " not in board:

            display_board(board)

            print("\nMatch Draw!")

            return None

       
        if player == "X":
            player = "O"
        else:
            player = "X"



def main():

    player1_score = 0
    player2_score = 0
    draws = 0

    while True:

        result = play_game()

        
        if result == "X":
            player1_score += 1

        elif result == "O":
            player2_score += 1

        else:
            draws += 1

    
        print("\n======= SCORE BOARD =======")
        print("Player 1 (X):", player1_score)
        print("Player 2 (O):", player2_score)
        print("Draws:", draws)

     
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("\nThank you for playing Tic Tac Toe!")
            break



main()
