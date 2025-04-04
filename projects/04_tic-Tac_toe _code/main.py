board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    
    win_conditions = [
        [0, 1, 2], 
        [3, 4, 5],  
        [6, 7, 8], 
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8], 
        [2, 4, 6]   
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def check_tie():
    return " " not in board


def play_game():
    current_player = "X"  

    while True:
        print_board()  

        move = input(f"Player {current_player}, choose a position (0-8): ")

        if not move.isdigit() or int(move) not in range(9):
            print("❌ Invalid input. Please enter a number from 0 to 8.")
            continue

        move = int(move)

        if board[move] != " ":
            print("⚠️ That spot is already taken. Choose another.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins! Congratulations!")
            break

    
        if check_tie():
            print_board()
            print("🤝 It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


# Step 6: Start the game
play_game()
