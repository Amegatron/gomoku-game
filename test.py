from GameBoardSerializer import GameBoardSerializer
from GameBoardStringRenderer import GameBoardStringRenderer
from GomokuGame import GomokuGame
import re

def get_player_char_by_number(player_num: int):
    return "X" if player_num == 1 else "O"


renderer = GameBoardStringRenderer()
game = GomokuGame(10, 10)

print("Starting Gomoku game! For now only playing against yourself :P")
print("Enter your moves in format like \"A9\", \"B7\", \"D19\" etc, without quotes.")
print("To stop the game, input \"exit\" or \"quit\".")
print(renderer.render(game.board))

game_result = 0
p = re.compile(r"^([a-z])(\d+)")
exit_code = False

while game_result == 0 and not exit_code:
    x = -1
    y = -1

    current_player_char = get_player_char_by_number(game.get_current_player())

    while True:
        raw_input = input("Enter your move (%s): " % current_player_char).lower()
        if raw_input in ("exit", "quit"):
            exit_code = True
            break

        m = p.search(raw_input)
        if not m:
            print("I can't understand your input :(")
        else:
            x = ord(m.group(1)) - ord("a")
            y = int(m.group(2))

        if game.can_make_move(x, y):
            break
        else:
            print("Can't make move on that cell.")

    if exit_code:
        break

    game_result = game.make_move(x, y)
    print(renderer.render(game.board))

if exit_code:
    print("Good bye!")
else:
    if game_result == -1:
        print("Draw!")
    else:
        print("%s wins!" % get_player_char_by_number(game_result))
