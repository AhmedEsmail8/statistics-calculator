from tkinter import *
from tkinter import font
from statistics import *
from matplotlib import *
from tkinter import messagebox
from matplotlib import pyplot
from math import *
from numpy import *
import numpy as np

i = 3  # counter submit x
j = 3  # counter submit y
p = 4  # counter correlation
u = 4  # counter regretion
x = []
y = []
labels = []


class d2_calc(Frame):
    def __init__(self, container, b, k):
        self.container = container
        self.k = k
        self.b = b
        Button(container, text='submit x', bg='#1598C0', command=lambda: d2_calc.submitx(
            container, b), cursor="hand2").grid(row=1, column=0, padx=(30), pady=(3))
        Button(container, text='submit y', bg='#1598C0', command=lambda: d2_calc.submity(
            container, k), cursor="hand2").grid(row=1, column=1, padx=(30), pady=(3))
        Button(container, text='correlation', bg='#1598C0', command=lambda: d2_calc.correlation(container), cursor="hand2").grid(
            row=1, column=2, padx=(30), pady=(3))
        Button(container, text='regression', bg='#1598C0', command=lambda: d2_calc.regression(container), cursor="hand2").grid(
            row=1, column=3, padx=(30), pady=(3))
        Button(container, text='reset', bg='#1598C0', command=lambda: d2_calc.reset(self), cursor="hand2").grid(
            row=0, column=3, padx=(30), pady=(3))

        Entry(container, textvariable=k).grid(
            row=0, column=1, padx=(30), pady=(3))
        Entry(container, textvariable=b).grid(
            row=0, column=0, padx=(30), pady=(3))

    def correlation(container):
        global p, x, y
        if len(x) != len(y) or len(x) <= 1 or len(y) <= 1:
            messagebox.showerror("Error", "Please enter data")
        else:
            r = np.corrcoef(x, y)[0, 1]
            r = round(np.corrcoef(x, y)[0, 1], 4)
            lab = Label(container, text=r)
            lab.grid(row=p, column=2)
            labels.append(lab)
            p += 1
            pyplot.scatter(x, y)
            pyplot.show()

    def regression(container):
        global u, r
        if len(x) != len(y) or len(x) <= 1 or len(y) <= 1:
            messagebox.showerror("Error", "Please enter data")
        else:
            b1 = np.corrcoef(x, y)[0, 1] * \
                (sqrt(variance(y))/sqrt(variance(x)))
            b0 = mean(y) - (b1*mean(x))

            if b1 < 0:
                total = 'Y = {}  {} X'.format(round(b0, 4), round(b1, 4))
            elif b1 > 0:
                total = 'Y = {} + {} X'.format(round(b0, 4), round(b1, 4))
            else:
                total = 'Y = {}'.format(round(b0, 4))

            lab = Label(container, text=total)
            lab.grid(row=u, column=3)
            labels.append(lab)
            u += 1

    def submitx(container, b):
        global i
        m = b.get()
        if d2_calc.checkFloat(m) == False:
            messagebox.showerror("Error", "Please enter valid data")
            b.set("")
        else:
            i += 1
            lab = Label(container, text=m, bg="#686868", fg="white", width=10)
            lab.grid(row=i, column=0, pady=1)
            labels.append(lab)
            x.append(float(m))
            b.set("")

    def submity(container, k):
        global j
        m = k.get()
        if d2_calc.checkFloat(m) == False:
            messagebox.showerror("Error", "Please enter valid data")
            k.set("")
        else:
            j += 1
            lab = Label(container, text=m, bg="#686868", fg="white", width=10)
            lab.grid(row=j, column=1, pady=1)
            labels.append(lab)
            y.append(float(m))
            k.set("")

    def reset(self):
        global i, j, p, u, x, y, labels
        i = 3
        j = 3
        p = 4
        u = 4
        x.clear()
        y.clear()
        for val in labels:
            val.destroy()
        labels.clear()

    def checkFloat(ans):
        try:
            float(ans)
            return True
        except:
            return False
