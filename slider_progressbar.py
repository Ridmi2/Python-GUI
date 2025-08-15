import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Slider and Progressbar ')
root.geometry('300x200')
root.resizable(False, False)
scale_value=tk.DoubleVar(value=50)

scale=ttk.Scale(root,command=lambda value:print(value),from_=0 ,to=100,length=300,variable=scale_value)
scale.pack()

progressbar=ttk.Progressbar(root,variable=scale_value)
progressbar.pack()
root.mainloop()