import tkinter as tk
from tkinter import ttk

# create a window
root = tk.Tk()

root.title('Basic Widgets')  # title of the window
root.iconbitmap('icon.ico')  # Ensure you have an icon file named 'icon.ico'
root.resizable(width=False, height=False)  # make the window resizable
root.geometry('300x200')  # size of the window (width*height)

#create a button
#old_button = tk.Button(root,text='Click me')
#old_button.pack()  # add to the window with some padding
def button_click_func():
    entry_field_value=entry.get()
    print(entry_field_value)
    label.configure(text=entry_field_value)
    button.configure(state='disabled')  # disable the button after click

entry=ttk.Entry(root)
entry.pack()  # modern entry widget with ttk
label = ttk.Label(root)
label.pack()  # add label to the window
button = ttk.Button(root,text='Click me',command=button_click_func)
button.pack() #modern with ttk




root.mainloop()  # run the window