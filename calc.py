from os import remove
from tkinter import *
from tkinter import font
# from tkinter.ttk import *
from statistics import *
from matplotlib import *
from math import *
from tkinter import messagebox

zeroes = int(1)
decimal = bool()
input = bool()
output = str("")
decimal = False
input = False
ro = 1
i = 0
data = []
negative = bool(False)
sum = float(0)
z = bool(False)
labels = []
id = int(0)


class calc(Frame):
    def __init__(self, container):
        self.container = container
        Label(container, text="0", background="blue", width=37).grid(
            row=0, column=0, padx=2, pady=2, columnspan=3)
        Button(container, text="7", cursor="hand2",
               command=lambda: calc.press(7, container), width=2).grid(row=1, column=0, sticky="nsew")
        Button(container, text="8", cursor="hand2",
               command=lambda: calc.press(8, container), width=6).grid(row=1, column=1, sticky="nsew")
        Button(container, text="9", cursor="hand2",
               command=lambda: calc.press(9, container), width=6).grid(row=1, column=2, sticky="nsew")
        Button(container, text="4", cursor="hand2",
               command=lambda: calc.press(4, container), width=6).grid(row=2, column=0, sticky="nsew")
        Button(container, text="5", cursor="hand2",
               command=lambda: calc.press(5, container), width=6).grid(row=2, column=1, sticky="nsew")
        Button(container, text="6", cursor="hand2",
               command=lambda: calc.press(6, container), width=6).grid(row=2, column=2, sticky="nsew")
        Button(container, text="1", cursor="hand2",
               command=lambda: calc.press(1, container), width=6).grid(row=3, column=0, sticky="nsew")
        Button(container, text="2", cursor="hand2",
               command=lambda: calc.press(2, container), width=6).grid(row=3, column=1, sticky="nsew")
        Button(container, text="3", cursor="hand2",
               command=lambda: calc.press(3, container), width=6).grid(row=3, column=2, sticky="nsew")
        Button(container, text="0", cursor="hand2",
               command=lambda: calc.press(0, container), width=6).grid(row=4, column=0, sticky="nsew")
        Button(container, text=".", cursor="hand2", command=lambda: calc.dec(container),
               width=6).grid(row=4, column=1, sticky="nsew")
        Button(container, text="ADD", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.add(container), width=6).grid(row=4, column=2, sticky="nsew")
        Button(container, text="\u2211"+" x", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq(1, container), width=6).grid(row=5, column=0, sticky="nsew")
        Button(container, text="x\u0305 ", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("mean", container), width=6).grid(row=5, column=1, sticky="nsew")
        Button(container, text="\u2213", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq(-1, container), width=6).grid(row=5, column=3, sticky="nsew")
        Button(container, text="MO", cursor="hand2",
               command=lambda: calc.eq("mod", container), width=6).grid(row=1, column=3, sticky="nsew")
        Button(container, text="\u03C3", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("stand", container), width=6).grid(row=2, column=3, sticky="nsew")
        Button(container, text="\u03C3\u00b2", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("var", container), width=6).grid(row=3, column=3, sticky="nsew")
        Button(container, text="z", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("z", container), width=6).grid(row=4, column=3, sticky="nsew")
        Button(container, text="C", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("c", container), width=6).grid(row=5, column=2, sticky="nsew")
        Button(container, text="Reset", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.reset(self, container)).grid(row=6, column=1, sticky="nsew", columnspan=2)
        Button(container, text="\u238C", cursor="hand2", font=("Bold", 10),
               command=calc.delete_val).grid(row=6, column=0, sticky="nsew")
        Button(container, text="\u232B", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.remove(container)).grid(row=0, column=3, sticky="nsew")
        Button(container, text="ME", cursor="hand2", font=("Bold", 10),
               command=lambda: calc.eq("med", container)).grid(row=6, column=3, sticky="nsew")

    def press(act, container):
        global i, zeroes, output, input, z
        if act != 0:
            input = True
            if decimal == False:
                i = i*10+act
            else:
                i = i+float((act/pow(10, zeroes)))
                zeroes += 1
        else:
            if decimal == False:
                i = i*10
            else:
                zeroes += 1
        if input == True:
            output = output+str(act)
            Label(container, text=output, background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)

        else:
            if decimal == False:
                lab = Label(container, text="0", background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
                labels.append(lab)
            else:
                output = output+str(act)
                Label(container, text=output, background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)

    def reset(self, container):
        global zeroes, decimal, input, output, ro, i, negative, sum, z, labels
        zeroes = 1
        output = ""
        decimal = False
        input = False
        ro = 1
        i = 0
        negative = False
        sum = 0
        z = False
        data.clear()
        print("after", data)
        for val in labels:
            val.destroy()
        labels.clear()
        Label(container, text="0", background="blue", width=37).grid(
            row=0, column=0, padx=2, pady=2, columnspan=3)

    def remove(container):
        global output, i, sum
        if len(output) > 0:
            i = int(i/10)
            output = output[:-1]
            if len(output) > 0:
                Label(container, text=output, background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
            else:
                Label(container, text="0", background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
        else:
            Label(container, text="0", background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)

    def eq(act, container):
        global output, negative, z
        if act == 1:
            Label(container, text=sum, background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
            print(sum)
            z=False
            output = ""
        elif act == -1:
            z=False
            if negative == False:
                negative = True
                output = "-"+output
                Label(container, text=output, background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
            else:
                negative = False
                output = output.replace(output[0], "")
                Label(container, text=output, background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "mean":
            z=False
            output = ""
            Label(container, text=mean(data), background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "mod":
            z=False
            output = ""
            Label(container, text=mode(data), background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "var":
            z=False
            output = ""
            Label(container, text=variance(data), background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "stand":
            z=False
            output = ""
            Label(container, text=sqrt(variance(data)), background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "z":
            z = True
            output = "Enter number :"
            Label(container, text=output, background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "med":
            z=False
            output = ""
            Label(container, text=median(data), background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)
        elif act == "c":
            z=False
            output = ""
            Label(container, text="0", background="blue", width=37).grid(
                row=0, column=0, padx=2, pady=2, columnspan=3)

    def dec(container):
        global decimal, zeroes, output, input
        decimal = True
        zeroes = 1
        if output.find('.') == -1:
            if (input == True):
                output = output+str(".")
            else:
                output = output+str("0.")
        Label(container, text=output, background="blue", width=37).grid(
            row=0, column=0, padx=2, pady=2, columnspan=3)

    def delete_val():
        global ro, labels, data, id, sum
        sum -= data[-1]
        labels[-1].destroy()
        data.pop()
        labels.pop()
        ro -= 1

    def checkFloat(ans):
        try:
            float(ans)
            return True
        except:
            return False

    def add(container):
        global i, ro, decimal, zeroes, output, input, sum, z, negative, id
        isValid = calc.checkFloat(output)
        if z == False and (output == "" or isValid == False or float(output) == 0):
            messagebox.showerror("Error", "Please enter valid data")
        else:
            negative = False
            size = len(output)
            if z == False:
                if input == True:
                    data.append(float(output))
                    if (output[size-1] == '.'):
                        s3 = output.replace(".", "")
                        lab = Label(
                            container, text=s3, background="#686868", foreground="white", width=20)
                        lab.grid(row=ro, column=5, padx=2,
                                 columnspan=3, pady=3)
                        labels.append(lab)
                    else:
                        lab = Label(container, text=float(
                            output), background="#686868", foreground="white", width=20)
                        lab.grid(row=ro, column=5, padx=2,
                                 columnspan=3, pady=3)
                        labels.append(lab)
                    ro += 1
                    id += 1
                Label(container, text="0", background="blue", width=37).grid(
                    row=0, column=0, padx=2, pady=2, columnspan=3)
                sum += float(output)
                input = False
                i = 0
                decimal = False
                zeroes = 1
                output = ""
                print(data)
            else:
                if len(data) == 0 or output=="Enter number :":
                    z = False
                    messagebox.showerror("Error", "Please enter data")
                    output = ""
                    Label(container, text="0", background="blue", width=37).grid(
                        row=0, column=0, padx=2, pady=2, columnspan=3)
                else:
                    output = output.replace("Enter number :", "")
                    print(output)
                    output = (float(output)-mean(data))/sqrt(variance(data))
                    Label(container, text=output, background="blue", width=37).grid(
                        row=0, column=0, padx=2, pady=2, columnspan=3)
                    z = False
                    output = ""
