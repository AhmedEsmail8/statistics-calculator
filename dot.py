import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import numpy as np
from collections import defaultdict

# freq = []
# name = []
label = []
ln = []
lst2 = []


class dot(Frame):
    def __init__(self, container, b):
        self.container = container
        self.b = b
        entry1 = Entry(container, textvariable=b)
        entry1.grid(row=0, column=0, padx=20, pady=10)
        button1 = Button(container, text='enter',fg='black', bg='#1598C0', activebackground="#1598C0",
                         cursor="hand2",command=lambda: dot.insert(container, b), font=20)
        button1.grid(row=1, column=0, pady=10)
        button2 = Button(container, text='Reset',fg='black', bg='#1598C0', activebackground="#1598C0",
                         cursor="hand2", command=lambda: dot.reset(self, b), font=20)
        button2.grid(row=1, column=2, pady=10)
        button3 = Button(container, text='Gragh', fg='black', bg='#1598C0', activebackground="#1598C0",
                         cursor="hand2",command=dot.dot)
        button3.grid(row=2, column=0)

    def checkFloat(ans):
        try:
            float(ans)
            return True
        except:
            return False

    def insert(container, b):
        isValid1 = dot.checkFloat(b.get())
        if isValid1 == False or b.get() == '0':
            messagebox.showerror("Error", "Please enter valid data")
            b.set("")
        else:
            ln.append(float(b.get()))
            for i in range(len(ln)):
                name = Label(
                    container, text=ln[i], bg="#686868", fg="white", width=20)
                label.append(name)
                name.grid(row=i+2, column=4, pady=1, columnspan=3)
            b.set("")

    def reset(slef, a):
        global ln
        ln.clear()
        ln.clear()
        for val in label:
            val.destroy()
        a.set("")

    def dot():
        di = {}
        di = defaultdict(lambda: 0, di)
        for val in ln:
            di[val] += 1
            lst2.append(di[val])
        fig = plt.scatter(ln, lst2)
        fig.axes.get_yaxis().set_visible(False)
        plt.show()
