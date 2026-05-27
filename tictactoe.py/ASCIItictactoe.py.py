def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    # All possible winning combos 
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    return all(space in ['X', 'O'] for space in board)


def main():
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    
    print("=====================")
    print(" TIC-TAC-TOE ")
    print("=====================")
    print("Enter the number (1-9) corresponding to the grid position.")

    while True:
        print_board(board)
        try:
            choice = int(input(f"Player {current_player}, choose a spot (1-9): "))
        except ValueError:
            print("❌ Invalid input, enter a number between 1 and 9.")
            continue
            
        if choice < 1 or choice > 9:
            print("❌ Out of bounds, choose a position between 1 and 9.")
            continue
            
        index = choice - 1
        if board[index] in ['X', 'O']:
            print("❌ That spot is already taken! Try again.")
            continue
            
        board[index] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!\n")
            break
            
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw, no winners\n")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
