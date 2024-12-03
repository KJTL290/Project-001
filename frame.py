from tkinter import *

root = Tk()
root.title("Practice Makes Perfect")
root.iconbitmap(r'C:\Users\User\Documents\GitHub\Python_Projects\favicon.ico')

# Create the LabelFrame and then pack it
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=1, pady=1)

# Create the Button and then pack it
b = Button(frame, text="I'm a button")
b.grid(row=0, column=0)
b2 = Button(frame, text="or here")
b2.grid(row=1, column=1)

root.mainloop()