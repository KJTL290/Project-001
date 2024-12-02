from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiply":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

  

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal =  Button(root, text="=", padx=91, pady=20, command=equal)
button_clear =  Button(root, text="clear", padx=79, pady=20, command=clear)

subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract)
multiply = Button(root, text="*", padx=39, pady=20, command=button_multiply)
divide = Button(root, text="/", padx=39, pady=20, command=button_divide)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
add.grid(row=5, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

subtract.grid(row=5, column=1)
multiply.grid(row=5, column=2)
divide.grid(row=6, column=0)

root.mainloop()

