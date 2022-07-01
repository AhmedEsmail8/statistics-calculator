from tkinter import *
from PIL import ImageTk, Image
from os import *
import calc
import pie
import bar
import dot
import box
import hist
import calc_2d


# hover functions
def on_enter(e):
    e.config(foreground="#252892")


def on_leave(e):
    e.config(background="#C7C7C7", foreground="black")


def show_calc():
    pie_obj.reset(a, b)
    bar_obj.reset(a, b)
    dot_obj.reset(a)
    box_obj.reset()
    hist_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    hist_frame.place_forget()
    box_frame.place_forget()
    bar_frame.place_forget()
    pie_frame.place_forget()
    dot_frame.place_forget()
    calc_frame.place(x=280, y=100)
    tabs.place(x=170, y=0)
    head.place_forget()


def show_pie():
    global head_txt
    head_lab.place_forget()
    head_lab.config(text="Pie Chart")
    head_lab.place(x=300, y=5)
    bar_obj.reset(a, b)
    dot_obj.reset(a)
    box_obj.reset()
    hist_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    calc_obj.reset(calc_frame)
    hist_frame.place_forget()
    box_frame.place_forget()
    bar_frame.place_forget()
    calc_frame.place_forget()
    dot_frame.place_forget()
    tabs.place_forget()
    pie_frame.place(x=350, y=100)
    head.place(x=170, y=0)


def show_bar():
    global head_txt
    head_lab.place_forget()
    head_lab.config(text="Bar Graph")
    head_lab.place(x=300, y=5)
    pie_obj.reset(a, b)
    calc_obj.reset(calc_frame)
    dot_obj.reset(a)
    box_obj.reset()
    hist_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    hist_frame.place_forget()
    box_frame.place_forget()
    pie_frame.place_forget()
    calc_frame.place_forget()
    dot_frame.place_forget()
    tabs.place_forget()
    bar_frame.place(x=350, y=100)
    head.place(x=170, y=0)


def show_dot():
    global head_txt
    head_lab.place_forget()
    head_lab.config(text="Dot Plot")
    head_lab.place(x=300, y=5)
    pie_obj.reset(a, b)
    calc_obj.reset(calc_frame)
    bar_obj.reset(a, b)
    box_obj.reset()
    hist_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    hist_frame.place_forget()
    tabs.place_forget()
    box_frame.place_forget()
    bar_frame.place_forget()
    pie_frame.place_forget()
    calc_frame.place_forget()
    dot_frame.place(x=280, y=100)
    head.place(x=170, y=0)


def show_box():
    global head_txt
    head_lab.place_forget()
    head_lab.config(text="Box Plot")
    head_lab.place(x=300, y=5)
    pie_obj.reset(a, b)
    calc_obj.reset(calc_frame)
    bar_obj.reset(a, b)
    dot_obj.reset(a)
    hist_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    hist_frame.place_forget()
    dot_frame.place_forget()
    tabs.place_forget()
    bar_frame.place_forget()
    pie_frame.place_forget()
    calc_frame.place_forget()
    box_frame.place(x=280, y=100)
    head.place(x=170, y=0)


def show_hist():
    global head_txt
    head_lab.place_forget()
    head_lab.config(text="Histogram")
    head_lab.place(x=300, y=5)
    pie_obj.reset(a, b)
    calc_obj.reset(calc_frame)
    bar_obj.reset(a, b)
    dot_obj.reset(a)
    box_obj.reset()
    obj_2d.reset()
    frame_2d.place_forget()
    dot_frame.place_forget()
    box_frame.place_forget()
    bar_frame.place_forget()
    tabs.place_forget()
    pie_frame.place_forget()
    calc_frame.place_forget()
    hist_frame.place(x=280, y=100)
    head.place(x=170, y=0)


def show_2D_calc():
    pie_obj.reset(a, b)
    calc_obj.reset(calc_frame)
    bar_obj.reset(a, b)
    dot_obj.reset(a)
    box_obj.reset()
    hist_obj.reset()
    hist_frame.place_forget()
    dot_frame.place_forget()
    box_frame.place_forget()
    bar_frame.place_forget()
    pie_frame.place_forget()
    calc_frame.place_forget()
    frame_2d.place(x=230, y=100)
    tabs.place(x=170, y=0)
    head.place_forget()


head_txt = str()
root = Tk()
root.geometry("900x700")
root.resizable(0, 0)
root.title("statistics calculator")
frame = Frame(root, width=170, height=900, bg="#C7C7C7")
frame.place(x=0, y=0)


calc_frame = Frame(root, width=750)
calc_obj = calc.calc(calc_frame)
calc_frame.place(x=280, y=100)

b = StringVar()
a = StringVar()
a.set("")
b.set("")

pie_frame = Frame(root, width=750)
pie_obj = pie.pie(pie_frame, a, b)

bar_frame = Frame(root, width=750)
bar_obj = bar.bar(bar_frame, a, b)

dot_frame = Frame(root, width=750)
dot_obj = dot.dot(dot_frame, a)

box_frame = Frame(root, width=750)
box_obj = box.box(box_frame, b)

hist_frame = Frame(root, width=750)
hist_obj = hist.hist(hist_frame, b)

frame_2d = Frame(root, width=750)
obj_2d = calc_2d.d2_calc(frame_2d, a, b)


tabs = Frame(root, bg="#686868", width=750, height=50)
D1 = Button(tabs, text="1D", relief=FLAT, fg="black",
            command=show_calc, width=40, cursor="hand2")
D1.place(x=20, y=12)
# D1.bind('<Enter>', lambda event: on_enter(D1))
# D1.bind('<Leave>', lambda event: on_leave(D1))
D2 = Button(tabs, text="2D", relief=FLAT, fg="black",
            command=show_2D_calc, width=40, cursor="hand2")
D2.place(x=400, y=12)
# D2.bind('<Enter>', lambda event: on_enter(D2))
# D2.bind('<Leave>', lambda event: on_leave(D2))
tabs.place(x=170, y=0)


head = Frame(root, bg="#686868", width=750, height=50)
head_lab = Label(head, font=('bold', 20),
                 fg="white", bg="#686868")

# logo
logo = Image.open("logo.png")
res_logo = logo.resize((200, 200), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(res_logo)
Label(frame, image=logo_img, bg="#C7C7C7").place(x=-15, y=0)


# calculator
# button
button = Button(frame, command=show_calc, relief=FLAT, text="calculator", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2")
button.place(x=40, y=220)
button.bind('<Enter>', lambda event: on_enter(button))
button.bind('<Leave>', lambda event: on_leave(button))
# icon
calc = Image.open("calculator.png")
res_calc = calc.resize((30, 30), Image.ANTIALIAS)
calc_img = ImageTk.PhotoImage(res_calc)
Label(frame, image=calc_img, bg="#C7C7C7").place(x=0, y=225)


# pie chart
# button
pie_btn = Button(frame, relief=FLAT, text="Pie Chart", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2", command=show_pie)
pie_btn.bind('<Enter>', lambda event: on_enter(pie_btn))
pie_btn.bind('<Leave>', lambda event: on_leave(pie_btn))
pie_btn.place(x=40, y=300)
# icon
pie = Image.open("pie.png")
res_pie = pie.resize((26, 26), Image.ANTIALIAS)
pie_img = ImageTk.PhotoImage(res_pie)
Label(frame, image=pie_img, bg="#C7C7C7").place(x=3, y=305)


# Histogram
# button
hist_btn = Button(frame, relief=FLAT, text="Histogram", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2", command=show_hist)
hist_btn.bind('<Enter>', lambda event: on_enter(hist_btn))
hist_btn.bind('<Leave>', lambda event: on_leave(hist_btn))
hist_btn.place(x=40, y=380)
# icon
hist = Image.open("histogram.png")
res_hist = hist.resize((26, 26), Image.ANTIALIAS)
hist_img = ImageTk.PhotoImage(res_hist)
Label(frame, image=hist_img, bg="#C7C7C7").place(x=3, y=385)


# box plot
# button
box_btn = Button(frame, relief=FLAT, text="Box Plot", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2", command=show_box)
box_btn.bind('<Enter>', lambda event: on_enter(box_btn))
box_btn.bind('<Leave>', lambda event: on_leave(box_btn))
box_btn.place(x=40, y=460)
# icon
box = Image.open("box.png")
res_box = box.resize((26, 26), Image.ANTIALIAS)
box_img = ImageTk.PhotoImage(res_box)
Label(frame, image=box_img, bg="#C7C7C7").place(x=3, y=465)


# bar graph
# button
bar_btn = Button(frame, relief=FLAT, text="Bar Graph", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2", command=show_bar)
bar_btn.bind('<Enter>', lambda event: on_enter(bar_btn))
bar_btn.bind('<Leave>', lambda event: on_leave(bar_btn))
bar_btn.place(x=40, y=540)
# icon
bar = Image.open("bar.png")
res_bar = bar.resize((26, 26), Image.ANTIALIAS)
bar_img = ImageTk.PhotoImage(res_bar)
Label(frame, image=bar_img, bg="#C7C7C7").place(x=3, y=545)


# dot graph
# button
dot_btn = Button(frame, relief=FLAT, text="Dot Plot", bg="#C7C7C7", font=(
    "bold", 18), fg="black", activebackground="#C7C7C7", border=0, activeforeground="#696FD4", cursor="hand2", command=show_dot)
dot_btn.bind('<Enter>', lambda event: on_enter(dot_btn))
dot_btn.bind('<Leave>', lambda event: on_leave(dot_btn))
dot_btn.place(x=40, y=620)
# icon
dot = Image.open("dot.png")
res_dot = dot.resize((26, 26), Image.ANTIALIAS)
dot_img = ImageTk.PhotoImage(res_dot)
Label(frame, image=dot_img, bg="#C7C7C7").place(x=3, y=625)

root.mainloop()
