from tkinter import *
from tkinter import messagebox

root = Tk()

entry = Entry(root, width=35, border=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # At first current should be empty
    # when you enter second number the first is added to current
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_num = entry.get()
    global f_num
    global math
    math = 'addition'
    # If user presses + without any values
    try:
        f_num = int(first_num)
    except ValueError:
        f_num = 0

    entry.delete(0, END)

def button_sub():
    first_num = entry.get()
    global f_num
    global math
    math = 'subtraction'
    # If user presses - without any values
    try:
        f_num = int(first_num)
    except ValueError:
        f_num = 0

    entry.delete(0, END)

def button_mul():
    first_num = entry.get()
    global f_num
    global math
    math = 'multiplacation'
    # If user presses * without any values
    try:
        f_num = int(first_num)
    except ValueError:
        f_num = 0

    entry.delete(0, END)

def button_div():
    first_num = entry.get()
    global f_num
    global math
    math = 'division'
    # If user presses / without any values
    try:
        f_num = int(first_num)
    except ValueError:
        f_num = 0

    entry.delete(0, END)

def button_equal():
    if entry.get() != '':
        # Incase the user clicks the equals button without any values
        second_num = entry.get()
        entry.delete(0, END)
        try:
            if math == 'addition':
                entry.insert(0, f_num + int(second_num))
            
            if math == 'subtraction':
                entry.insert(0, f_num - int(second_num))

            if math == 'multiplacation':
                entry.insert(0, f_num * int(second_num))
            
            if math == 'division':
                entry.insert(0, f_num / int(second_num))
        except NameError:
            # When user does not select an operation
            pass

def close():
    if messagebox.askyesno(title='Quit?', message="Are you sure?"):
        root.destroy()

# Setting some shortcuts to read user inout from keyboard
def shortcut(event):
    # print(event.state)
    # print(event.keysym)
    for num in range(0, 10):
        if event.state == 0 and event.keysym == str(num):
            button_click(num)

    if event.state == 1 and event.keysym == 'plus':
        button_add()
    if event.state == 0 and event.keysym == 'minus':
        button_sub()
    if event.state == 0 and event.keysym == 'slash':
        button_div()
    if event.state == 1 and event.keysym == 'asterisk':
        button_mul()

    if event.state == 4 and event.keysym == 'c':
        button_clear()
        
    if event.state == 0 and event.keysym == 'equal':
        button_equal()

root.bind('<KeyPress>', shortcut)

# Define the buttons
b1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
b0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

b_add = Button(root, text='+', padx=39, pady=20, command=lambda: button_add())
b_equal = Button(root, text='=', padx=89, pady=20, command=button_equal)
b_clear = Button(root, text='clear', padx=79, pady=20, command=button_clear)

b_sub = Button(root, text='-', padx=40, pady=20, command=lambda: button_sub())
b_mul = Button(root, text='*', padx=41, pady=20, command=lambda: button_mul())
b_div = Button(root, text='/', padx=41, pady=20, command=lambda: button_div())

# Display the buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

b_clear.grid(row=5, column=1, columnspan=2) # Clear
b_add.grid(row=5, column=0) # Add
b_equal.grid(row=6, column=1, columnspan=2) # Answer

b_sub.grid(row=6, column=0)
b_mul.grid(row=4, column=1)
b_div.grid(row=4, column=2)

root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()