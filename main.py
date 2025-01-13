from tkinter import *


def convert():
    x = entry.get()
    if x != "":
        cel=int(x)
        far=(9/5*(cel))+32
        print(far)

root=Tk()
root.title("Some GUI")
root.geometry("400x700")

Button(root, text="Total", command=convert).pack()
entry = Entry(root)
entry.pack()
Label(root,text="Enter a Celcius temperature.").pack()

root.mainloop()