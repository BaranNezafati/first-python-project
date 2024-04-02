#Baran Nezafati ( Calculator project )
from fpdf import FPDF
from tkinter import *
import math

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial',size=20)

win = Tk()
win.title('Calculator')
win.resizable(False, False)
win.geometry('438x573+460+40')

coverFrame = Frame(
    win,
    bd=20,
    pady=2,
    relief=RIDGE)

coverMainFrame = Frame(
    coverFrame,
    bd=10,
    pady=2,
    bg='cadetblue',
    relief=RIDGE)

MainFrame = Frame(
    coverMainFrame,
    bd=5,
    pady=2,
    relief=RIDGE)

class Calculator():
    def maths_PM(self):
        self.result = False
        self.current = -(float(entDisplay.get()))
        self.display(self.current)

    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def number_enter(self, num):
        self.result = False
        first_num = entDisplay.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def display(self, value):
        entDisplay.delete(0, END)
        entDisplay.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0

    def clear_last_char(self):
        self.result = False
        current_len = len(entDisplay.get())
        entDisplay.delete(current_len - 1, END)
        if current_len == 1:
            self.current = '0'
            self.input_value = True

    def square_root(self):
        self.result = False
        num = float(entDisplay.get())
        result = math.sqrt(num)
        self.display(result)

    def operate(self, operator):
        self.result = False
        self.total = float(entDisplay.get())
        self.current = ''
        self.check_sum = True
        self.op = operator

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(entDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(entDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(entDisplay.get())))
        self.display(self.current)

    def calculate(self):
        self.result = True
        current_value = float(entDisplay.get())
        if self.check_sum:
            if self.op == '+':
                self.total += current_value
            elif self.op == '-':
                self.total -= current_value
            elif self.op == '*':
                self.total *= current_value
            elif self.op == '/':
                if current_value != 0:
                    self.total /= current_value
                else:
                    self.display("Error")
                    return
            self.display(self.total)
        else:
            self.total = current_value

added_value = Calculator()

entDisplay = Entry(
    MainFrame,
    font=('arial', 18, 'bold'),
    bd=14,
    width=26,
    bg='pink',
    justify=RIGHT)
entDisplay.insert(0, '0')

numpad = '789456123'
i = 0
btn = []
for j in range(3, 6):
    for k in range(3):
        btn.append(Button(MainFrame,
                  width=6,
                  height=2,
                  font=('arial', 16, 'bold'),
                  bd=4,
                  bg='snow3',
                  text=numpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]['command'] = lambda x=numpad[i]: added_value.number_enter(x)
        i += 1

# btn---------------------------------------------------------------------------

btnBackSpace = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='<--',
    bd=4,
    command=added_value.clear_last_char)

btnClear = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text=chr(67),
    bd=4,
    command=added_value.clear_entry)

btnClearAll = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text=chr(67) + chr(69),
    bd=4,
    command=added_value.clear_all)

btnPM = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text=chr(177),
    bd=4,
    command=added_value.maths_PM)


btnSq = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='√',
    bd=4,
    command=added_value.square_root)

btnCos = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='Cos',
    bd=4,
    command=added_value.cos)

btnTan = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='Tan',
    bd=4,
    command=added_value.tan)

btnSin = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='Sin',
    bd=4,
    command=added_value.sin)

btnAdd = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='+',
    bd=4,
    command=lambda: added_value.operate('+'))

btnSub = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='-',
    bd=4,
    command=lambda: added_value.operate('-'))

btnMult = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='*',
    bd=4,
    command=lambda: added_value.operate('*'))

btnDiv = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text=chr(247),
    bd=4,
    command=lambda: added_value.operate('/'))

btnZero = Button(
    MainFrame,
    width=6,
    height=2,
    bg='snow3',
    font=('arial', 16, 'bold'),
    text='0',
    bd=4,
    command=lambda: added_value.number_enter(0))

btnDot = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='.',
    bd=4,
    command=lambda: added_value.number_enter('.'))

btnEquals = Button(
    MainFrame,
    width=6,
    height=2,
    bg='salmon',
    font=('arial', 16, 'bold'),
    text='=',
    bd=4,
    command=added_value.calculate)

# grid------------------------------------------------------
coverFrame.grid()
coverMainFrame.grid()
MainFrame.grid()
entDisplay.grid(row=0, column=0, columnspan=4, pady=1)
btnBackSpace.grid(row=1, column=0, pady=1)
btnClear.grid(row=1, column=1, pady=1)
btnClearAll.grid(row=1, column=2, pady=1)
btnPM.grid(row=1, column=3, pady=1)
btnSq.grid(row=2, column=0, pady=1)
btnCos.grid(row=2, column=1, pady=1)
btnTan.grid(row=2, column=2, pady=1)
btnSin.grid(row=2, column=3, pady=1)
btnAdd.grid(row=3, column=3, pady=1)
btnSub.grid(row=4, column=3, pady=1)
btnMult.grid(row=5, column=3, pady=1)
btnDiv.grid(row=6, column=3, pady=1)
btnZero.grid(row=6, column=0, pady=1)
btnDot.grid(row=6, column=1, pady=1)
btnEquals.grid(row=6, column=2, pady=1)

win.mainloop()
