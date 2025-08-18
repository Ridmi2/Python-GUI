import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.title=('Events')
root.geometry('300x200')
root.resizable(False, False)


entry=ttk.Entry(root)
entry.pack()
entry.bind('<FocusIn>', lambda event: print("Entry button selected"))
entry.bind('<FocusOut>', lambda event: print("Entry button deselected"))
button=ttk.Button(root,text='Click Me')
button.pack()
root.bind('<Enter>',lambda event:print("Enter to button"))
root.bind('<Leave>',lambda event:print("Leave from buttton"))

root.mainloop()
