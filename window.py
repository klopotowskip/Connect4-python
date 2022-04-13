import tkinter as tk
import constant as const


def draw_circle(x, y, r, fill, canvas_name):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill=fill)


class Window:
    def __init__(self):
        self.root = tk.Tk()

    def render(self, board):
        canvas = tk.Canvas(
            self.root,
            height=const.BOARD_HEIGHT * 100 + 110,
            width=const.BOARD_WIDTH * 100 + 10,
            bg="#263d42"
        )
        canvas.pack()

        main_frame = tk.Frame(canvas, bg="#ddd")

        main_frame.place(relwidth=1, height=const.BOARD_HEIGHT * 100 + 10, x=0, y=100)

        for i in range(0, const.BOARD_HEIGHT):
            for j in range(0, const.BOARD_WIDTH):
                x, y = (100 * j + 10, 100 * i + 10)

                frame = tk.Frame(main_frame, bg="#999")
                frame.place(width=90, height=90, x=x, y=y)

                fill = "#333"
                if board[i][j] == 1:
                    fill = "#e00"
                elif board[i][j] == 2:
                    fill = "#ee0"
                tile = tk.Canvas(frame, height=90, width=90, bg="#999")
                draw_circle(
                    x=45,
                    y=45,
                    r=35,
                    fill=fill,
                    canvas_name=tile
                )
                tile.pack()
        self.root.mainloop()
