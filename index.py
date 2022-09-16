import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("330x150")
root.resizable(0,0)
root.title("Calculator App")

#Functions
def add():
    n1 = i1.get()
    n2 = i2.get()
    if not len(n1) or not len(n2):
        messagebox.showwarning(message="Please Enter values")
        return
    try:
        s = int(n1)+int(n2)
    except ValueError:
        messagebox.showwarning(message="Please Enter values in Integer")
        return
    messagebox.showinfo(root,message="The sum is "+str(s))

def sub():
    n1 = i1.get()
    n2 = i2.get()
    if not len(n1) or not len(n2):
        messagebox.showwarning(message="Please Enter values")
        return
    try:
        s = int(n1)-int(n2)
    except ValueError:
        messagebox.showwarning(message="Please Enter values in Integer")
        return
    messagebox.showinfo(root,message="The difference is "+str(s))

def mul():
    n1 = i1.get()
    n2 = i2.get()
    if not len(n1) or not len(n2):
        messagebox.showwarning(message="Please Enter values")
        return
    try:
        s = int(n1)*int(n2)
    except ValueError:
        messagebox.showwarning(message="Please Enter values in Integer")
        return
    messagebox.showinfo(root,message="The product is "+str(s))

def div():
    n1 = i1.get()
    n2 = i2.get()
    if not len(n1) or not len(n2):
        messagebox.showwarning(message="Please Enter values")
        return
    try:
        s = int(n1)/int(n2)
    except ValueError:
        messagebox.showwarning(message="Please Enter values in Integer")
        return
    messagebox.showinfo(root,message="The Quotient is "+str(s))

i1 = tk.StringVar()
i2 = tk.StringVar()

h1 = tk.Label(root,text="Calculator",font=('Aerial',18,'bold')).grid(row=0,column=1)

l1 = tk.Label(root,text="Number 1: ").grid(row=1,column=1)
e1 = tk.Entry(root,textvariable=i1).grid(row=1,column=2)

l2 = tk.Label(root,text="Number 2: ").grid(row=2,column=1)
e2 = tk.Entry(root,textvariable=i2).grid(row=2,column=2)

i1.set("")
i2.set("")

d1 = tk.Label().grid(row=3,column=1)
b1 = tk.Button(root,text="Add",command=add).grid(row=4,column=0,padx=6)

b2 = tk.Button(root,text="Sub",command=sub).grid(row=4,column=1)

b3 = tk.Button(root,text="Mul",command=mul).grid(row=4,column=2)

b4 = tk.Button(root,text="Div",command=div).grid(row=4,column=3)

root.mainloop()
