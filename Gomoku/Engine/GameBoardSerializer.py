from Gomoku.Engine.GameBoard import GameBoard


class GameBoardSerializer:
    def serialize(self, board: GameBoard):
        result = bytearray([board.x, board.y])

        quartet = 0
        counter = 0
        for j in range(board.x):
            for i in range(board.y):
                val = board.board[i][j] << (3 - counter) * 2
                quartet = quartet | val
                counter += 1

                if counter == 4:
                    result.append(quartet)
                    quartet = 0
                    counter = 0

        return result
