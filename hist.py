import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import numpy as np

label = []
l = []


class hist(Frame):
    def __init__(self, container, b):
        self.container = container
        self.b = b
        entry1 = Entry(container, textvariable=b)
        entry1.grid(row=0, column=0, padx=20)
        button1 = Button(container, text='enter', fg='black',
                         bg='#1598C0', activebackground="#1598C0", cursor="hand2", command=lambda: hist.insert(container, b), font=20)
        button1.grid(row=1, column=0)
        button2 = Button(container, text='Reset', fg='black',
                         bg='#1598C0', activebackground="#1598C0", cursor="hand2", command=lambda: hist.reset(self), font=20)
        button2.grid(row=1, column=2)
        button3 = Button(container, text='Gragh', command=hist.histo,
                         bg='#1598C0', activebackground="#1598C0", cursor="hand2", font=20)
        button3.grid(row=1, column=3, padx=60)

    def checkFloat(ans):
        try:
            float(ans)
            return True
        except:
            return False

    def insert(container, b):
        tmp = 0
        isValid1 = hist.checkFloat(b.get())
        if isValid1 == False:
            messagebox.showerror("Error", "Please enter valid data")
            b.set("")
        else:
            l.append(float(b.get()))
            for i in range(len(l)):
                freq = Label(container, text=l[i],
                             bg="#686868", fg="white", width=30)
                label.append(freq)
                freq.grid(row=i + 4, column=tmp, columnspan=4, pady=5)
                if i > 15:
                    tmp += 1
                    i = 0
            b.set("")

    def reset(self):
        global l
        l.clear()
        for val in label:
            val.destroy()

    def histo():
        plt.hist(l)
        plt.show()
