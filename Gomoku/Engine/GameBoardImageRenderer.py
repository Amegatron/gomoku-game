from PIL import Image, ImageDraw


class GameBoardImageRenderer:
    def __init__(self, cell_size=24, padding=6, thickness=2, color="#cccccc"):
        self.cell_size = cell_size
        imX = Image.new("RGB", (cell_size, cell_size), 0)
        dX = ImageDraw.Draw(imX)
        dX.line([padding, padding, cell_size-padding, cell_size-padding], fill=color, width=thickness)
        dX.line([padding, cell_size-padding, cell_size-padding, padding], fill=color, width=thickness)

        imO = Image.new("RGB", (cell_size, cell_size), 0)
        dO = ImageDraw.Draw(imO)
        dO.ellipse([padding, padding, cell_size-padding, cell_size-padding], fill=0, outline=color, width=thickness)

        self.chars = [imX, imO]

    def render(self, board):
        im = Image.new("RGB", (board.x * self.cell_size, board.y * self.cell_size))

        for i in range(board.x):
            for j in range(board.y):
                p = board.board[i][j]
                if p > 0:
                    im.paste(self.chars[p - 1], (i * self.cell_size, j * self.cell_size))

        grid_color = "#808080"
        imD = ImageDraw.Draw(im)
        for i in range(1, board.x):
            imD.line([i*self.cell_size, 0, i*self.cell_size, board.y * self.cell_size], fill=grid_color)

        for j in range(1, board.y):
            imD.line([0, j*self.cell_size, board.x * self.cell_size, j*self.cell_size], fill=grid_color)

        imD.line([0, 0, self.cell_size * board.x, 0])
        imD.line([0, 0, 0, self.cell_size * board.y])
        imD.line([0, self.cell_size * board.y - 1, self.cell_size * board.x - 1, self.cell_size * board.y - 1])
        imD.line([self.cell_size * board.x - 1, 0, self.cell_size * board.x - 1, self.cell_size * board.y - 1])

        return im