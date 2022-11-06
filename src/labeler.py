from PIL import ImageTk, Image
from tkinter import Tk, Canvas, IntVar, Scale, RIDGE, HORIZONTAL, NW, Scrollbar, Listbox, Button, END, messagebox
import glob

tk = Tk()

# Image paths
paths = glob.glob("./inputs/*")

# The image display canvas
canvas = Canvas(tk, width=448, height=448, relief=RIDGE, bd=1)
canvas.grid(column=0, row=0, rowspan=3)
# The bbox rect
x1_var = IntVar()
y1_var = IntVar()
x2_var = IntVar()
y2_var = IntVar()


def update_rect(useless):
	canvas.delete("all")

	tk.display_image = ImageTk.PhotoImage(Image.open(paths[0]).resize((448, 448)))
	canvas.create_image(0, 0, anchor=NW, image=tk.display_image)
	canvas.create_rectangle(x1_var.get(), y1_var.get(), x2_var.get(), y2_var.get(), outline="red")

# The image bbox params
x1_slider = Scale(tk, label="x1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=x1_var, command=update_rect)
x1_slider.grid(column=1, row=0)

y1_slider = Scale(tk, label="y1", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=y1_var, command=update_rect)
y1_slider.grid(column=2, row=0)

x2_slider = Scale(tk, label="x2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=x2_var, command=update_rect)
x2_slider.grid(column=1, row=1)

y2_slider = Scale(tk, label="y2", orient=HORIZONTAL, from_=0, to=447, resolution=1.0, sliderlength=10, length=200, variable=y2_var, command=update_rect)
y2_slider.grid(column=2, row=1)

# List for data bounds
bboxes_scroll = Scrollbar(tk)
bboxes_list = Listbox(tk, yscrollcommand=bboxes_scroll.set)
bboxes_scroll.config(command=bboxes_list.yview)
bboxes_scroll.grid(column=5, row=0, rowspan=2)
bboxes_list.grid(column=3, row=0, rowspan=2, columnspan=2)


def add_bbox():
	if x1_var.get() < x2_var.get() and y1_var.get() < y2_var.get():
		bboxes_list.insert(END, " ".join([str(x1_var.get()), str(y1_var.get()), str(x2_var.get()), str(y2_var.get())]))
	else:
		messagebox.showinfo("Error", "x1 < x2 and y1 < y2 must be true")

def remove_bbox():
	if len(bboxes_list.curselection()) > 0:
		bboxes_list.delete(bboxes_list.curselection()[0])

def save_bboxes():
	with open(paths[0] + ".info", "w") as f:
		f.write(" ".join(bboxes_list.get(0, END)))
	paths.pop(0)
	bboxes_list.delete(0, END)
	if len(paths) == 0:
		messagebox.showinfo("Done", "Ur done.")
		tk.quit()

# Buttons for data functions
bbox_save_btn = Button(tk, text="Save", command=save_bboxes)
bbox_add_btn = Button(tk, text="Add bbox", command=add_bbox)
bbox_remove_btn = Button(tk, text="Remove bbox", command=remove_bbox)
bbox_save_btn.grid(column=1, row=2, columnspan=2)
bbox_add_btn.grid(column=3, row=2)
bbox_remove_btn.grid(column=4, row=2)

tk.mainloop()
