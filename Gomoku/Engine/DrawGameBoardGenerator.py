import copy
import random

from Gomoku.Engine.GameBoard import GameBoard

# These indexes are chosen so that the closest direction to rollback is lower
# See "rollback" section of algo
DIR_LEFT = 0
DIR_TOP_RIGHT = 1
DIR_TOP = 2
DIR_TOP_LEFT = 3


class DrawGameBoardGenerator:
    def generate(self, width: int, height: int, mask=None):
        """
            Draw game board generator, which is guaranteed to return a valid draw-state of game.
        """
        board = GameBoard(width, height)
        counter = {
            DIR_TOP: 0,
            DIR_TOP_LEFT: 0,
            DIR_TOP_RIGHT: 0,
            DIR_LEFT: 0,
        }

        if mask is None:
            mask = [[1 for j in range(height)] for i in range(width)]

        row_counter_board = [[copy.copy(counter) for j in range(height)] for i in range(width)]
        p_counters = {1: 0, 2: 0}
        idx = 0
        board_stack = []
        cell_stack = None
        iteration_counter = 0
        longest_rollback = 0
        non_symmetry_rollbacks = 0

        while True:
            while idx < width * height:
                i = idx % width
                j = idx // width

                if mask[i][j] == 1:
                    break

                idx += 1
                board_stack.append([])

            if idx == width * height:
                # Rollback to fix symmetry in count of moves
                if abs(p_counters[1] - p_counters[2]) > 1:
                    non_symmetry_rollbacks += 1

                    while abs(p_counters[1] - p_counters[2]) > 1 and p_counters[1] + p_counters[2] > 0:
                        cell_stack = board_stack.pop()
                        idx -= 1
                        i = idx % width
                        j = idx // width

                        if mask[i][j]:
                            removed_p = board.board[i][j]
                            board.make_move(i, j, 0)
                            p_counters[removed_p] -= 1
                else:
                    # Finish generation
                    break

            max_counters = {1: 0, 2: 0}
            max_counters_dirs = {1: None, 2: None}
            player_counters = {1: copy.copy(counter), 2: copy.copy(counter)}

            if cell_stack is None:
                if idx > 10:
                    selector = random.randint(0, p_counters[1] + p_counters[2])
                    first_move = 1 if selector > p_counters[1] else 2
                else:
                    first_move = random.randint(1, 2)
                next_move = 2 - first_move + 1
                cell_stack = [next_move, first_move]

            if j == 0:
                if i != 0:
                    a = row_counter_board[i - 1][0][DIR_LEFT]
                    p = board.board[i - 1][0]
                    if p > 0:
                        max_counters[p] = a
                        player_counters[p][DIR_LEFT] = a
                        max_counters_dirs[p] = DIR_LEFT
            else:
                if i != 0:
                    a = row_counter_board[i - 1][j][DIR_LEFT]
                    p = board.board[i - 1][j]
                    if p > 0:
                        player_counters[p][DIR_LEFT] = a
                        if a > max_counters[p]:
                            max_counters[p] = a
                            max_counters_dirs[p] = DIR_LEFT

                    a = row_counter_board[i - 1][j - 1][DIR_TOP_LEFT]
                    p = board.board[i - 1][j - 1]
                    if p > 0:
                        player_counters[p][DIR_TOP_LEFT] = a
                        if a > max_counters[p]:
                            max_counters[p] = a
                            max_counters_dirs[p] = DIR_TOP_LEFT

                if i < width - 1:
                    a = row_counter_board[i + 1][j - 1][DIR_TOP_RIGHT]
                    p = board.board[i + 1][j - 1]
                    if p > 0:
                        player_counters[p][DIR_TOP_RIGHT] = a
                        if a > max_counters[p]:
                            max_counters[p] = a
                            max_counters_dirs[p] = DIR_TOP_RIGHT

                a = row_counter_board[i][j - 1][DIR_TOP]
                p = board.board[i][j - 1]
                if p > 0:
                    player_counters[p][DIR_TOP] = a
                    if a > max_counters[p]:
                        max_counters[p] = a
                        max_counters_dirs[p] = DIR_TOP

            can_place = False
            move = 0
            while len(cell_stack) > 0:
                move = cell_stack.pop()
                if max_counters[move] < 4:
                    can_place = True
                    break

            if can_place:
                p_counters[move] += 1
                new_counters = copy.copy(player_counters[move])
                for k, v in new_counters.items():
                    new_counters[k] += 1

                board.make_move(i, j, move)
                row_counter_board[i][j] = new_counters
                board_stack.append(cell_stack)
                cell_stack = None
                idx += 1
                iteration_counter += 1

            # Rollback to rearrange latter moves
            else:
                rollback_len = 0

                # We need to rollback not just one cell before, but until the closest cell
                # which makes a 4-in-row already
                target_idx = None
                dir1 = max_counters_dirs[1]
                dir1 = dir1 if dir1 is not None else 100000
                dir2 = max_counters_dirs[2]
                dir2 = dir2 if dir2 is not None else 100000
                closest_dir = min(dir1, dir2)

                if closest_dir == DIR_LEFT:
                    target_idx = idx - 1
                elif closest_dir == DIR_TOP:
                    target_idx = idx - width
                elif closest_dir == DIR_TOP_RIGHT:
                    target_idx = idx - width + 1
                else:
                    target_idx = idx - width - 1

                while idx > target_idx + 1:
                    cell_stack = board_stack.pop()
                    idx -= 1
                    rollback_len += 1

                    if mask[idx % width][idx // width]:
                        removed_p = board.board[idx % width][idx // width]
                        board.make_move(idx % width, idx // width, 0)
                        p_counters[removed_p] -= 1

                # Next we still continue to rollback normally - removing empty stacks
                while idx >= 0:
                    cell_stack = board_stack.pop()
                    idx -= 1
                    rollback_len += 1
                    if mask[idx % width][idx // width]:
                        removed_p = board.board[idx % width][idx // width]
                        board.make_move(idx % width, idx // width, 0)
                        p_counters[removed_p] -= 1

                    if len(cell_stack) > 0:
                        if rollback_len > longest_rollback:
                            longest_rollback = rollback_len
                        break

        return board, (iteration_counter, longest_rollback, non_symmetry_rollbacks), p_counters
