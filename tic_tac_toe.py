import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    # Check rows
    for row in board:
        if all([s == player for s in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def check_draw(board):
    for row in board:
        for spot in row:
            if spot == ' ':
                return False
    return True

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. That spot is already taken or out of bounds.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def get_computer_move(board):
    available_moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                available_moves.append((r, c))

    # Simple AI: Check for winning move, then block user's winning move, then center, then corners, then sides.
    # Check for computer's winning move
    for r, c in available_moves:
        board[r][c] = 'O'
        if check_win(board, 'O'):
            return r, c
        board[r][c] = ' ' # backtrack

    # Check for user's winning move to block it
    for r, c in available_moves:
        board[r][c] = 'X'
        if check_win(board, 'X'):
            return r, c
        board[r][c] = ' ' # backtrack
    
    # Try center
    if (1, 1) in available_moves:
        return 1, 1

    # Try corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for r, c in corners:
        if (r, c) in available_moves:
            return r, c

    # Try sides
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for r, c in sides:
        if (r, c) in available_moves:
            return r, c

    # Fallback to random if no strategic moves left (should not happen with full logic)
    return random.choice(available_moves)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = 'X' # User is 'X', Computer is 'O'

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', the computer is 'O'.")
    print("Enter a number 1-9 to place your mark on the board:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("---------")

    while True:
        print_board(board)

        if player_turn == 'X':
            print("Your turn (X):")
            row, col = get_user_move(board)
            board[row][col] = 'X'
        else:
            print("Computer's turn (O)...")
            row, col = get_computer_move(board)
            board[row][col] = 'O'
            print(f"Computer chose {row*3 + col + 1}")

        if check_win(board, player_turn):
            print_board(board)
            if player_turn == 'X':
                print("Congratulations! You win!")
            else:
                print("Computer wins! Better luck next time.")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player_turn = 'O' if player_turn == 'X' else 'X'

if __name__ == "__main__":
    play_game()
