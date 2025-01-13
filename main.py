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
                result_label.config(text="Пожалуйста используйте валидную температуру")
        except ValueError:
            result_label.config(text="Неверный ввод. Введите число")
    else:
        result_label.config(text="Введите температуру")

root = Tk()
root.title("Преобразователь температур")
root.geometry("400x300")

Label(root, text="Введите температуру в Фаренгейтах").pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)

unit_var = StringVar(value="C")
Label(root, text="Выберите нужную температуру:").pack(pady=5)
Radiobutton(root, text="Цельсии (°C)", variable=unit_var, value="C").pack()
Radiobutton(root, text="Кельвины (K)", variable=unit_var, value="K").pack()

Button(root, text="Преобразовать", command=convert).pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
