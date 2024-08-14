import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for 'X', -1 for 'O'
    
    def print_board(self):
        for row in self.board:
            print(' '.join(['X' if cell == 1 else 'O' if cell == -1 else '-' for cell in row]))
    
    def is_winner(self, player):
        return any(np.all(self.board[i, :] == player) for i in range(3)) or \
               any(np.all(self.board[:, i] == player) for i in range(3)) or \
               np.all(np.diag(self.board) == player) or \
               np.all(np.diag(np.fliplr(self.board)) == player)
    
    def is_draw(self):
        return not np.any(self.board == 0)
    
    def make_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            return True
        return False
    
    def switch_player(self):
        self.current_player *= -1
    
    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]
    
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1

def collect_game_data(episodes):
    data = []
    for _ in range(episodes):
        game = TicTacToe()
        state = game.board.copy()
        while True:
            moves = game.get_available_moves()
            action = random.choice(moves)
            game.make_move(*action)
            next_state = game.board.copy()
            reward = 0
            if game.is_winner(game.current_player):
                reward = 1 if game.current_player == 1 else -1
                data.append((state.flatten(), action, reward))
                break
            elif game.is_draw():
                data.append((state.flatten(), action, 0))
                break
            state = next_state
            game.switch_player()
    return data

data = collect_game_data(1000)
