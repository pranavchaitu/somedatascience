import chess
import chess.engine

# Initialize the board
board = chess.Board()

def print_board():
    print(board)

def get_move():
    move = input("Enter your move in UCI format (e.g., e2e4): ")
    return move

def play_game():
    print_board()
    
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            print("White's move")
        else:
            print("Black's move")
        
        move = get_move()
        
        try:
            board.push_uci(move)
        except ValueError:
            print("Invalid move! Please try again.")
            continue
        
        print_board()
    
    result = board.result()
    print(f"Game over! Result: {result}")

if __name__ == "__main__":
    play_game()

