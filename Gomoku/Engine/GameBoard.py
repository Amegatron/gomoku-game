class GameBoard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[0 for j in range(y)] for i in range(x)]

    def make_move(self, x, y, player):
        self.board[x][y] = player
