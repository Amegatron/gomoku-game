from GameBoard import GameBoard


class GomokuRuleSet:
    def can_place(self, game_board: GameBoard, x, y):
        return game_board.board[x][y] == 0

    def check_game_ended(self, game_board: GameBoard):
        """
            Checks if the game has ended.

            Returns player number if there is a winner, 0 if there is still no winner,
            and -1 if it is a draw (no more moves left)
        """
        empty_counter = 0

        for i in range(game_board.x):
            for j in range(game_board.y):
                current_player = game_board.board[i][j]
                if current_player == 0:
                    empty_counter += 1
                    continue

                if i <= game_board.x - 4:
                    if game_board.board[i + 1][j] == current_player and \
                            game_board.board[i + 2][j] == current_player and \
                            game_board.board[i + 3][j] == current_player and \
                            game_board.board[i + 4][j] == current_player:
                        return current_player

                    if j >= 4:
                        if game_board.board[i + 1][j - 1] == current_player and \
                                game_board.board[i + 2][j - 2] == current_player and \
                                game_board.board[i + 3][j - 3] == current_player and \
                                game_board.board[i + 4][j - 4] == current_player:
                            return current_player

                if j <= game_board.y - 4:
                    if game_board.board[i][j+1] == current_player and \
                            game_board.board[i][j+2] == current_player and \
                            game_board.board[i][j+3] == current_player and \
                            game_board.board[i][j+4] == current_player:
                        return current_player

                if i <= game_board.x - 4 and j <= game_board.y - 4:
                    if game_board.board[i+1][j+1] == current_player and \
                            game_board.board[i+2][j+2] == current_player and \
                            game_board.board[i+3][j+3] == current_player and \
                            game_board.board[i+4][j+4] == current_player:
                        return current_player

                # No need to check other directions because they are opposite to what
                # we have already checked

        return 0 if empty_counter > 0 else -1
