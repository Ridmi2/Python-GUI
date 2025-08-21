import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Tree View")
root.geometry('500x400')
root.resizable(False,False)

table=ttk.Treeview(root,columns=('Name', 'Age', 'Email'), show='headings')
table.heading('Name', text='Name')
table.heading('Age', text='Age')
table.heading('Email', text='Email')
table.column('Age',width=100)
table.pack()

Name=['Ridmi', 'Nadeesha', 'Saman', 'Kamal']
Age=[25, 26, 27, 28]

for idx,value in enumerate(Name):
    table.insert('', idx, values=(Name[idx], Age[idx], f'{Name[idx]}@gmail.com'))


table.bind('<<TreeviewSelect>>', lambda event: print(event))


root.mainloop()