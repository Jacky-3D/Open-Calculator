import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear_input():
    entry.delete(0, tk.END)
    result.set("")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

result = tk.StringVar()
result.set("")

result_label = tk.Label(root, textvariable=result, width=20, font=("Arial", 14))
result_label.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+',
]

row_val = 2
col_val = 0

button_width = 4
button_height = 2

for button in buttons:
    tk.Button(root, text=button, width=button_width, height=button_height, font=("Arial", 12), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', width=button_width, height=button_height, font=("Arial", 12), command=clear_input).grid(row=row_val, column=col_val)
col_val += 1

tk.Button(root, text='=', width=button_width, height=button_height, font=("Arial", 12), command=evaluate_expression).grid(row=row_val, column=col_val)

root.mainloop()
