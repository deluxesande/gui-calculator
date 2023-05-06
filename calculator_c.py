import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.root = tk.Tk()

        # Entry
        self.entry = tk.Entry(self.root, width=30, border=5)

        # tk.Buttons
        self.b1 = tk.Button(self.root, text='1', padx=40, pady=20, command=lambda: self.button_click(1))
        self.b2 = tk.Button(self.root, text='2', padx=40, pady=20, command=lambda: self.button_click(2))
        self.b3 = tk.Button(self.root, text='3', padx=40, pady=20, command=lambda: self.button_click(3))
        self.b4 = tk.Button(self.root, text='4', padx=40, pady=20, command=lambda: self.button_click(4))
        self.b5 = tk.Button(self.root, text='5', padx=40, pady=20, command=lambda: self.button_click(5))
        self.b6 = tk.Button(self.root, text='6', padx=40, pady=20, command=lambda: self.button_click(6))
        self.b7 = tk.Button(self.root, text='7', padx=40, pady=20, command=lambda: self.button_click(7))
        self.b8 = tk.Button(self.root, text='8', padx=40, pady=20, command=lambda: self.button_click(8))
        self.b9 = tk.Button(self.root, text='9', padx=40, pady=20, command=lambda: self.button_click(9))
        self.b0 = tk.Button(self.root, text='0', padx=40, pady=20, command=lambda: self.button_click(0))

        # Operation buttons
        self.b_add = tk.Button(self.root, text='+', padx=39, pady=20, command=lambda: self.add_button())
        self.b_equal = tk.Button(self.root, text='=', padx=89, pady=20, command=self.equals_button)
        self.b_clear = tk.Button(self.root, text='clear', padx=79, pady=20, command=self.clear_button)

        self.b_sub = tk.Button(self.root, text='-', padx=40, pady=20, command=lambda: self.sub_button())
        self.b_mul = tk.Button(self.root, text='*', padx=41, pady=20, command=lambda: self.mul_button())
        self.b_div = tk.Button(self.root, text='/', padx=41, pady=20, command=lambda: self.div_button())

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()
    
    def on_close(self):
        if messagebox.askyesno(title='Quit?', message="Are you sure?"):
            self.root.destroy()

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))

    def add_button(self):
        first_num = self.entry.get()
        global f_num, math
        math = 'addition'

        try:
            f_num = int(first_num)
        except ValueError:
            f_num = 0

        self.entry.delete(0, tk.END)

    def sub_button(self):
        first_num = self.entry.get()
        global f_num, math
        math = 'subtraction'

        try:
            f_num = int(first_num)
        except ValueError:
            f_num = 0

        self.entry.delete(0, tk.END)

    def div_button(self):
        first_num = self.entry.get()
        global f_num, math
        math = 'division'

        try:
            f_num = int(first_num)
        except ValueError:
            f_num = 0

        self.entry.delete(0, tk.END)

    def mul_button(self):
        first_num = self.entry.get()
        global f_num, math
        math = 'multiplacation'

        try:
            f_num = int(first_num)
        except ValueError:
            f_num = 0

        self.entry.delete(0, tk.END)

    def equals_button(self):
        if self.entry.get() != '':
            second_num = self.entry.get()
            self.entry.delete(0, tk.END)

            try:
                if math == 'addition':
                    self.entry.insert(0, f_num + int(second_num))
                if math == 'subtraction':
                    self.entry.insert(0, f_num - int(second_num))
                if math == 'division':
                    self.entry.insert(0, f_num / int(second_num))
                if math == 'multiplacation':
                    self.entry.insert(0, f_num * int(second_num))
            except NameError:
                pass

    def clear_button(self):
        self.entry.delete(0, tk.END)



if __name__== '__main__':
    Calculator()