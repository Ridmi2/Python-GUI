import tkinter as tk
from tkinter import ttk
from calendar import month_name



root = tk.Tk()
root.geometry('300x200')
root.title('Combo Box Example')
root.resizable(False, False)

selected_month=tk.StringVar()


month_names=[month_name[i] for i in range (1,13) ]
print(month_names)

combobox=ttk.Combobox(root,values=month_names,textvariable=selected_month)
combobox.pack()

label=ttk.Label(root,textvariable=selected_month)
label.pack()



root.mainloop()