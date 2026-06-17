import math as m
import tkinter as tk

def solve_equation():
    a = int(entry_a.get())
    b = int(entry_b.get())
    c = int(entry_c.get())

    d = b**2 - 4*a*c
    if d == 0:
        root = -b / (2*a)
        result_label.config(text=f"Equal roots: {root}")
    elif d > 0:
        f = (-b + m.sqrt(d)) / (2*a)
        g = (-b - m.sqrt(d)) / (2*a)
        result_label.config(text=f"Distinct roots: {f}, {g}")
    else:
        result_label.config(text="No real roots")

windows = tk.Tk()
windows.title("Equation Solver")
windows.geometry("400x300")

tk.Label(windows, text="Enter a:").pack()
entry_a = tk.Entry(windows)
entry_a.pack()

tk.Label(windows, text="Enter b:").pack()
entry_b = tk.Entry(windows)
entry_b.pack()

tk.Label(windows, text="Enter c:").pack()
entry_c = tk.Entry(windows)
entry_c.pack()

tk.Button(windows, text="Solve", command=solve_equation).pack()

result_label = tk.Label(windows, text="")
result_label.pack()

windows.mainloop()




