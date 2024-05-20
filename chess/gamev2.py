import pygame
import chess

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 800
square_size = width // 8
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_SQUARE = (118, 150, 86)
LIGHT_SQUARE = (238, 238, 210)
HIGHLIGHT_COLOR = (180, 180, 0)

# Initialize the chess board
board = chess.Board()

# Load fonts
font = pygame.font.SysFont('Arial', 36)

# Unicode characters for chess pieces
piece_unicode = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                piece_str = piece_unicode[piece.symbol()]
                text_surface = font.render(piece_str, True, BLACK)
                screen.blit(text_surface, (col * square_size + square_size // 4, row * square_size + square_size // 4))

def get_square_under_mouse():
    mouse_pos = pygame.mouse.get_pos()
    x, y = [v // square_size for v in mouse_pos]
    if 0 <= x < 8 and 0 <= y < 8:
        return chess.square(x, 7 - y)
    return None

def draw_highlight(square):
    if square is not None:
        col = chess.square_file(square)
        row = 7 - chess.square_rank(square)
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * square_size, row * square_size, square_size, square_size), 3)

def main():
    running = True
    selected_square = None

    while running:
        draw_board()
        draw_pieces()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_under_mouse()
                if square is not None:
                    if selected_square is None:
                        selected_square = square
                    else:
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            board.push(move)
                        selected_square = None

        if selected_square:
            draw_highlight(selected_square)

        pygame.display.flip()

        if board.is_game_over():
            print("Game over!")
            print(board.result())
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()

