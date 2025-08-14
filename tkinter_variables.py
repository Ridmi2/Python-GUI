#to ensure the connectivity between widgets , or share the same value between widgets

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('300x200')
root.title('Variables')

variable_value=tk.StringVar(value='Hello, World!')

label=ttk.Label(root, textvariable=variable_value)
label.pack()

entry=ttk.Entry(root, textvariable=variable_value)
entry.pack()

button=ttk.Button(root, text='Click me', command=lambda: print(variable_value.get()))
button.pack()

root.mainloop()