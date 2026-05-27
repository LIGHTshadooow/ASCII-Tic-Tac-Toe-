def print_board(board):
    """Prints the current state of the board with a clean ASCII grid."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    """Checks if the given player has won the game."""
    # All possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    """Checks if the game is a draw (no empty spaces left)."""
    # If there are no numbers left, the board is full
    return all(space in ['X', 'O'] for space in board)


def main():
    # Initialize the board with numbers 1-9 so players know how to choose a spot
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    
    print("===============================")
    print("  WELCOME TO ASCII TIC-TAC-TOE ")
    print("===============================")
    print("To play, enter the number (1-9) corresponding to the grid position.")

    while True:
        print_board(board)
        
        # Get and validate user input
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 9.")
            continue
            
        # Check if the number is within the valid range
        if choice < 1 or choice > 9:
            print("❌ Out of bounds! Choose a position between 1 and 9.")
            continue
            
        # Check if the spot is already taken
        index = choice - 1
        if board[index] in ['X', 'O']:
            print("❌ That spot is already taken! Try again.")
            continue
            
        # Make the move
        board[index] = current_player
        
        # Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉\n")
            break
            
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("🤝 It's a draw! Well played. 🤝\n")
            break
            
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()