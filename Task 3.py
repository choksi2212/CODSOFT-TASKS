import tkinter as tk
from tkinter import messagebox
import random

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    upper_case_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case_chars = "abcdefghijklmnopqrstuvwxyz"
    number_chars = "0123456789"
    symbol_chars = "!@#$%^&*()-_=+"

    chars = ""
    if include_uppercase:
        chars += upper_case_chars
    if include_lowercase:
        chars += lower_case_chars
    if include_numbers:
        chars += number_chars
    if include_symbols:
        chars += symbol_chars

    if chars == "":
        return "Please select at least one character type."

    password = ""
    for _ in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]

    return password

def generate_password_callback():
    length = int(length_entry.get())
    include_uppercase = upper_case_var.get()
    include_lowercase = lower_case_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
    password_label.config(text=password)

root = tk.Tk()

length_label = tk.Label(root, text="Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_case_var = tk.BooleanVar()
upper_case_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=upper_case_var)
upper_case_checkbox.pack()

lower_case_var = tk.BooleanVar()
lower_case_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lower_case_var)
lower_case_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password_callback)
generate_button.pack()

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()