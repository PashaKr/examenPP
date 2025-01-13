from tkinter import *

def convert():
    x = entry.get()
    if x != "":
        try:
            cel = float(x)
            far = (9 / 5 * cel) + 32
            result_label.config(text=f"{cel:.2f}°C = {far:.2f}°F")
        except ValueError:
            result_label.config(text="Invalid input! Please enter a number.")

root = Tk()
root.title("Celsius to Fahrenheit")
root.geometry("400x200")

entry = Entry(root)
entry.pack()

Label(root, text="Enter a Celsius temperature:").pack()

Button(root, text="Convert", command=convert).pack()

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
