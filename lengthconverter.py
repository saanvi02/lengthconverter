import tkinter as tk

root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text=f"Length in cm: {cm:.2f}")

title_label = tk.Label(root, text="Inches to Centimeters")
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter length in inches:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Length in cm:")
result_label.pack()

root.mainloop()
