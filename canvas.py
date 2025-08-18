import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title("Canvas")
root.geometry('500x400')
root.resizable(False,False)

canvas=tk.Canvas(root,bg="white")
canvas.pack()

brush_width=4
def draw(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill="black")

def start_drawing(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill="black")    
    canvas.bind('<B1-Motion>', draw)    

#canvas.create_rectangle(10,10,100,200,fill="blue",outline="black")
#canvas.create_oval(120,110,200,200,fill="red",outline="black")
#canvas.create_polygon(250,50,300,100,350,50,fill="green",outline="black")
canvas.bind('<Button-1>',start_drawing)
#canvas.create_line(0,0,100,350,fill="black",width=6)
root.mainloop()