import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Tournament Scoring System")
root.columnconfigure(0, weight= 1)
root.rowconfigure(0, weight = 1)


lab = ttk.Label(text = "Hello")
lab.grid(row = 0, column = 1)




root.mainloop()