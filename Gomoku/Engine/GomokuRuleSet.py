from Gomoku.Engine.GameBoard import GameBoard


class GomokuRuleSet:
    def can_place(self, game_board: GameBoard, x, y):
        return 0 <= x < game_board.x and game_board.board[x][y] == 0 and 0 <= y < game_board.y

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

                if i < game_board.x - 4:
                    if game_board.board[i + 1][j] == current_player and \
                            game_board.board[i + 2][j] == current_player and \
                            game_board.board[i + 3][j] == current_player and \
                            game_board.board[i + 4][j] == current_player:
                        return current_player, (i, j, "right")

                    if j >= 4:
                        if game_board.board[i + 1][j - 1] == current_player and \
                                game_board.board[i + 2][j - 2] == current_player and \
                                game_board.board[i + 3][j - 3] == current_player and \
                                game_board.board[i + 4][j - 4] == current_player:
                            return current_player, (i, j, "top_right")

                if j < game_board.y - 4:
                    if game_board.board[i][j+1] == current_player and \
                            game_board.board[i][j+2] == current_player and \
                            game_board.board[i][j+3] == current_player and \
                            game_board.board[i][j+4] == current_player:
                        return current_player, (i, j, "down")

                    if i < game_board.x - 4:
                        if game_board.board[i+1][j+1] == current_player and \
                                game_board.board[i+2][j+2] == current_player and \
                                game_board.board[i+3][j+3] == current_player and \
                                game_board.board[i+4][j+4] == current_player:
                            return current_player, (i, j, "down_right")

                # No need to check other directions because they are opposite to what
                # we have already checked

        return 0 if empty_counter > 0 else -1, None
