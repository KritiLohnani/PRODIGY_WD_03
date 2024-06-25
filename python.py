class ChessGame:

    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'

    def initialize_board(self):
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        return board

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, piece, start_pos, end_pos):
        # Add logic to validate moves based on piece type and board position
        # For now, we'll keep this as a placeholder returning True
        return True  # Placeholder for validation logic

    def make_move(self, start_pos, end_pos):
        piece = self.board[start_pos[0]][start_pos[1]]
        if self.is_valid_move(piece, start_pos, end_pos):
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = '.'
            self.current_player = 'black' if self.current_player == 'white' else 'white'
        else:
            print('Invalid move. Try again.')

if __name__ == '__main__':
    chess_game = ChessGame()

    while True:
        chess_game.display_board()
        print(f"{chess_game.current_player}'s turn.")
        
        start_pos = input('Enter start position (e.g., "a2"): ')
        end_pos = input('Enter end position (e.g., "a4"): ')

        # Convert user input to board indices
        start_row, start_col = int(start_pos[1]) - 1, ord(start_pos[0]) - ord('a')
        end_row, end_col = int(end_pos[1]) - 1, ord(end_pos[0]) - ord('a')

        chess_game.make_move((start_row, start_col), (end_row, end_col))
