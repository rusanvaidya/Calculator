from tkinter import *
import math   
operations = []
Calculator = Tk()      
 
Calculator.geometry('290x470')
Calculator.title('Calculator')
Calculator.resizable(0, 0)

def num(n):
    digit = len(screen.get())
    screen.insert(digit ,n)
    return

def clear():
    operations.clear()
    screen.delete(0,END)
    return

def getnum():
    num = float(screen.get())
    operations.append(num)
    print(operations)
    return num

def operating(opera):
    getnum()
    operations.append(opera)
    screen.delete(0,END)
    print(type(operations[0]))
    print(operations)

def result():
    r=0
    getnum()
    num1, opera, num2 = operations[-3], operations[-2], operations[-1]
    r = 0
    if opera == "+":
        r = add(num1,num2)
    if opera == "-":
        r = subs(num1,num2)
    if opera == "*":
        r = mul(num1, num2)
    if opera == "/":
        r = div(num1,num2)
    print(r)

    screen.delete(0, END)
    screen.insert(0 ,r)
    return

def add(num1, num2):
    return num1+num2

def subs(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


screen = Entry(Calculator, width=18)

btn_1 = Button(Calculator, text='1', width=4, height=4, command=lambda: num(1))
btn_2 = Button(Calculator, text='2', width=4, height=4, command=lambda: num(2))
btn_3 = Button(Calculator, text='3', width=4, height=4, command=lambda: num(3))
btn_4 = Button(Calculator, text='4', width=4, height=4, command=lambda: num(4))
btn_5 = Button(Calculator, text='5', width=4, height=4, command=lambda: num(5))
btn_6 = Button(Calculator, text='6', width=4, height=4, command=lambda: num(6))
btn_7 = Button(Calculator, text='7', width=4, height=4, command=lambda: num(7))
btn_8 = Button(Calculator, text='8', width=4, height=4, command=lambda: num(8))
btn_9 = Button(Calculator, text='9', width=4, height=4, command=lambda: num(9))
btn_0 = Button(Calculator, text='0', width=4, height=4, command=lambda: num(0))

dot_btn = Button(Calculator, text='.', width=4, height=4, command=lambda: num("."))
btn_ce = Button(Calculator, text='CE', width=4, height=4, foreground='red', command=lambda: clear())

add_btn = Button(Calculator, text='+', width=4, height=4, command=lambda: operating("+"))
subs_btn = Button(Calculator, text='-', width=4, height=4, command=lambda: operating("-"))
mul_btn = Button(Calculator, text='x', width=4, height=4, command=lambda: operating("*"))
divide_btn = Button(Calculator, text='/', width=4, height=4, command=lambda: operating("/"))
equal_btn = Button(Calculator, text='=', width=4, height=4, command=lambda: result())
# btn = Button(Calculator, text = 'Click me !', command = Calculator.destroy)
# btn.grid(side = 'top')

screen.grid(row=1, column=1, columnspan=3)
btn_ce.grid(row=1, column=4)


btn_7.grid(row=2,column=1)
btn_8.grid(row=2,column=2)
btn_9.grid(row=2, column=3)


btn_4.grid(row=3, column=1)
btn_5.grid(row=3, column=2)
btn_6.grid(row=3, column=3)

btn_1.grid(row=4, column=1)
btn_2.grid(row=4, column=2)
btn_3.grid(row=4,column=3)

dot_btn.grid(row=5, column=1)
btn_0.grid(row=5, column=2)

add_btn.grid(row=2, column=4)
subs_btn.grid(row=3, column=4)
mul_btn.grid(row=4, column=4)
divide_btn.grid(row=5, column=4)
equal_btn.grid(row=5, column=3)

Calculator.mainloop()
