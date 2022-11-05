from PIL import ImageTk, Image
from tkinter import *
import glob

tk = Tk()

# Image paths
paths = glob.glob("./inputs/*")

# The image display canvas
canvas = Canvas(tk, width=448, height=448, relief=RIDGE, bd=1)
canvas.grid(column=0, row=0, rowspan=2)

# The image bbox params
x1_slider = Scale(tk, label="x1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200)
x1_slider.grid(column=1, row=0)

y1_slider = Scale(tk, label="y1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200)
y1_slider.grid(column=2, row=0)

x2_slider = Scale(tk, label="x2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200)
x2_slider.grid(column=1, row=1)

y2_slider = Scale(tk, label="y2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200)
y2_slider.grid(column=2, row=1)

tk.mainloop()
