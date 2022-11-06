from PIL import ImageTk, Image
from tkinter import Tk, Canvas, IntVar, Scale, RIDGE, HORIZONTAL, NW
import glob

tk = Tk()

# Image paths
paths = glob.glob("./inputs/*")

# The image display canvas
canvas = Canvas(tk, width=448, height=448, relief=RIDGE, bd=1)
canvas.grid(column=0, row=0, rowspan=2)
# The bbox rect
x1_var = IntVar()
y1_var = IntVar()
x2_var = IntVar()
y2_var = IntVar()

def update_rect(useless):
	canvas.delete("all")

	img = ImageTk.PhotoImage(Image.open(paths[0]))
	canvas.create_image(50, 50, anchor=NW, image=img)
	canvas.create_rectangle(x1_var.get(), y1_var.get(), x2_var.get(), y2_var.get())

# The image bbox params
x1_slider = Scale(tk, label="x1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=x1_var, command=update_rect)
x1_slider.grid(column=1, row=0)

y1_slider = Scale(tk, label="y1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=y1_var, command=update_rect)
y1_slider.grid(column=2, row=0)

x2_slider = Scale(tk, label="x2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=x2_var, command=update_rect)
x2_slider.grid(column=1, row=1)

y2_slider = Scale(tk, label="y2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=y2_var, command=update_rect)
y2_slider.grid(column=2, row=1)

tk.mainloop()
