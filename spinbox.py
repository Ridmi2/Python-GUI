import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Spring Box Example')
root.geometry('300x200')
root.resizable(False, False)

spinbox_value=tk.StringVar()


spinbox=ttk.Spinbox(root, from_=5 ,to=15,increment=2,textvariable=spinbox_value)
spinbox.pack()

label=ttk.Label(root,textvariable=spinbox_value)
label.pack()

root.mainloop()