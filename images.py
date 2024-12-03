from tkinter import Tk, Canvas, PhotoImage
from tkinter.constants import NW

root = Tk()
root.title("Practice")

canvas = Canvas(root, width=50, height=50)
canvas.pack()

photo_img = PhotoImage(file='OIP.jpg')
my_img = canvas.create_image(0, 0, image=photo_img, anchor=NW)

root.mainloop()