import tkinter
import random

ROW = 25
COLUMN = 25
TILE_SIZE = 25

WINDOW_HEIGHT = TILE_SIZE * ROW
WINDOW_WIDTH = TILE_SIZE * COLUMN

#--------------------------console window---------------------
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window, bg = "black", width=WINDOW_WIDTH, height= WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#----------------------keep the winow in center---------------
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenheight()

window.mainloop()