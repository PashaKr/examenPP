from tkinter import *

def convert():
    temp_f = entry.get()
    target_unit = unit_var.get()

    if temp_f != "":
        try:
            temp_f = float(temp_f)
            if target_unit == "C":
                temp_c = (temp_f - 32) * 5 / 9
                result_label.config(text=f"{temp_f:.2f}°F = {temp_c:.2f}°C")
            elif target_unit == "K":
                temp_k = (temp_f - 32) * 5 / 9 + 273.15
                result_label.config(text=f"{temp_f:.2f}°F = {temp_k:.2f} K")
            else:
                result_label.config(text="Please select a valid unit.")
        except ValueError:
            result_label.config(text="Invalid input! Please enter a number.")
    else:
        result_label.config(text="Please enter a temperature.")

root = Tk()
root.title("Temperature Converter")
root.geometry("400x300")

Label(root, text="Enter a Fahrenheit temperature:").pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)

unit_var = StringVar(value="C")
Label(root, text="Select target unit:").pack(pady=5)
Radiobutton(root, text="Celsius (°C)", variable=unit_var, value="C").pack()
Radiobutton(root, text="Kelvin (K)", variable=unit_var, value="K").pack()

Button(root, text="Convert", command=convert).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
