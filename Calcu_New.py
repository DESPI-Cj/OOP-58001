from tkinter import*
window = Tk()
window.geometry("255x315+10+10")
window.title("Calculator")

class Calculator:
    def __init__(self,win):
        self.txt1 = Entry(win, bd=20, width="35", bg= "light blue")
        self.txt1.grid(row=0, sticky="nw")

        self.btn1 = Button(win, bd=1, height="-15", text="C", width="20", font=("Arial",15, "bold"))
        self.btn1.grid(sticky="nw", padx=5)
        self.btn1.bind('<Button-1>', self.clear)

        self.btn2 = Button(win, bd=1, width="8", text="7", height="2")
        self.btn2.grid(row=2, sticky="w", padx=5,pady=2)
        self.btn2.bind('<Button-1>', self.seven)

        self.btn3 = Button(win, bd=1, width="8", text="8", height="2")
        self.btn3.grid(row=2, sticky="w",padx=70, pady=2)
        self.btn3.bind('<Button-1>', self.eigth)

        self.btn4 = Button(win, bd=1, width="8", text="9", height="2")
        self.btn4.grid(row=2, sticky="w",padx=135, pady=2)
        self.btn4.bind('<Button-1>', self.nine)

        self.btn5 = Button(win, bd=1, width="6", text="/", height="2")
        self.btn5.grid(row=2, sticky="w",padx=200, pady=2)
        self.btn5.bind('<Button-1>', self.divide)

        self.btn6 = Button(win, bd=1, width="8", text="4", height="2")
        self.btn6.grid(row=3, sticky="w",padx=5,pady=2)
        self.btn6.bind('<Button-1>', self.four)

        self.btn7 = Button(win, bd=1, width="8", text="5", height="2")
        self.btn7.grid(row=3, sticky="w",padx=70, pady=2)
        self.btn7.bind('<Button-1>', self.five)

        self.btn8 = Button(win, bd=1, width="8", text="6", height="2")
        self.btn8.grid(row=3, sticky="w",padx=135, pady=2)
        self.btn8.bind('<Button-1>', self.six)

        self.btn9 = Button(win, bd=1, width="6", text="*", height="2")
        self.btn9.grid(row=3, sticky="w",padx=200, pady=2)
        self.btn9.bind('<Button-1>', self.multiply)

        self.btn10 = Button(win, bd=1, width="8", text="1", height="2")
        self.btn10.grid(row=4, sticky="w",padx=5,pady=2)
        self.btn10.bind('<Button-1>', self.one)

        self.btn11 = Button(win, bd=1, width="8", text="2", height="2")
        self.btn11.grid(row=4, sticky="w",padx=70, pady=2)
        self.btn11.bind('<Button-1>', self.two)

        self.btn12 = Button(win, bd=1, width="8", text="3", height="2")
        self.btn12.grid(row=4, sticky="w",padx=135, pady=2)
        self.btn12.bind('<Button-1>', self.three)

        self.btn13 = Button(win, bd=1, width="6", text="-", height="2")
        self.btn13.grid(row=4, sticky="w", padx=200, pady=2)
        self.btn13.bind('<Button-1>', self.subtraction)

        self.btn14 = Button(win, bd=1, width="10", text="0", height="2")
        self.btn14.grid(row=5, sticky="w",padx=5,pady=2)
        self.btn14.bind('<Button-1>', self.zero)

        self.btn15 = Button(win, bd=1, width="11", text=".", height="2")
        self.btn15.grid(row=5, sticky="w",padx=85, pady=2)
        self.btn15.bind('<Button-1>', self.decimal)

        self.btn16 = Button(win, bd=1, width="10", text="+", height="2")
        self.btn16.grid(row=5, sticky="w", padx=172, pady=2)
        self.btn16.bind('<Button-1>', self.addition)

        self.btn1 = Button(win, bd=1, justify="center", width ="20", height="-15", text="=", font=("Arial",15, "bold"))
        self.btn1.grid(sticky="nw", padx=5)
        self.btn1.bind('<Button-1>', self.result)

        self.value = 0
        self.operation = 0
        self.n1 = 0
        self.n2 = 0

    def one(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "1")
    def two(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "2")
    def three(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "3")
    def four(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "4")
    def five(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "5")
    def six(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "6")
    def seven(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "7")
    def eigth(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "8")
    def nine(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "9")
    def zero(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "0")
    def clear(self, event):
        self.txt1.delete(0, END)
        self.n1 = 0
        self.n2 = 0
        self.operation = 0
    def decimal(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + ".")

    def addition(self, event):
        self.n1 += float(self.txt1.get())
        self.txt1.delete(0, END)
        self.operation = "+"
    def subtraction(self, event):
        if self.n1 == 0:
            self.n1 = float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "-"
            print(self.n1)
        else:
            self.n1 -= float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "-"
            print(self.n1)

    def multiply(self, event):
        if self.n1 == 0:
            self.n1 = 1
            self.n1 *= float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "*"
        else:
            self.n1 *= float(self.txt.get())
            self.txt1.delete(0, END)
            self.operation = "*"
    def divide(self, event):
        if self.n1 == 0:
            self.n1 = float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "/"
        else:
            self.n1 /= float(self.txt.get())
            self.txt1.delete(0, END)
            self.operation = "/"

    def result(self, event):
        if self.operation == "+":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 + self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "-":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 - self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "*":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 * self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "/":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1/self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())

        self.n1 = 0


mywin = Calculator(window)
window.mainloop()
