# TIC-TAC-TOE AI USING MINIMAX (Unbeatable AI)

# Board Representation
board = [" " for _ in range(9)]

# Print Board
def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")
    print("\n")

# Check Winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # Rows
        [0,3,6],[1,4,7],[2,5,8],  # Columns
        [0,4,8],[2,4,6]           # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check Draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner("O"):   # AI wins
        return 1
    if check_winner("X"):   # Human wins
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move (Best Move Selection)
def ai_move():
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Human Move
def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos >= 0 and pos < 9 and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Enter a number between 1 and 9.")

# Game Loop
def play():
    print("TIC-TAC-TOE")
    print("You = X | AI = O")
    print("Positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        print_board()
        human_move()

        if check_winner("X"):
            print_board()
            print("You Win!")
            break
        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("AI Wins!")
            break
        if is_draw():
            print_board()
            print("It's a Draw!")
            break

play()
