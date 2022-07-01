from tkinter import font
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import numpy as np

# freq = []
# name = []
label = []
l = []
ln = []


class bar(Frame):
    def __init__(self, container, a, b):
        self.container = container
        self.a = a
        self.b = b
        Label(container, text="frequency:").grid(row=0, column=0)
        Label(container, text="Data:").grid(row=0, column=2)
        entry1 = Entry(container, textvariable=b)
        entry1.grid(row=1, column=0, padx=20)
        entry2 = Entry(container, textvariable=a)
        entry2.grid(row=1, column=2)
        button1 = Button(container, text='enter', fg='black', bg='#1598C0', activebackground="#1598C0",
                         command=lambda: bar.insert(a, b, container), font=20, cursor="hand2")
        button1.grid(row=2, column=0, pady=10)
        button2 = Button(container, text='Reset', fg='black', bg='#1598C0', activebackground="#1598C0",
                         command=lambda: bar.reset(self, a, b), font=20, cursor="hand2")
        button2.grid(row=2, column=2)
        button3 = Button(container, text='Gragh', bg='#1598C0', activebackground="#1598C0", font=20,
                         command=bar.bar, cursor="hand2")
        button3.grid(row=2, column=3, padx=60)

    def checkFloat(ans):
        try:
            float(ans)
            return True
        except:
            return False

    def insert(a, b, container):
        isValid1 = bar.checkFloat(b.get())
        isValid2 = bar.checkFloat(a.get())
        if len(b.get()) == 0 or len(a.get()) == 0:
            messagebox.showerror("Error", "Please enter valid data")
            a.set("")
            b.set("")
        else:
            if isValid1 == False or isValid2 == True:
                messagebox.showerror("Error", "Please enter valid data")
                a.set("")
                b.set("")
            else:
                l.append(float(b.get()))
                ln.append(a.get())
                for i in range(len(ln)):
                    name = Label(
                        container, text=ln[i], bg="#686868", fg="white", width=20)
                    label.append(name)
                    name.grid(row=i+3, column=2, columnspan=2, pady=1)

                a.set("")
                for i in range(len(l)):
                    freq = Label(
                        container, text=l[i], bg="#686868", fg="white", width=20)
                    label.append(freq)
                    freq.grid(row=i+3, column=0, columnspan=2, pady=1)
                b.set("")

    def reset(self, a, b):
        global l, ln
        l.clear()
        ln.clear()
        for val in label:
            val.destroy()
        b.set("")
        a.set("")

    def bar():
        fig = plt.figure(figsize=(10, 5))
        plt.bar(ln, l, color='maroon', width=0.4)
        plt.show()
