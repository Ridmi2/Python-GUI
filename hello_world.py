import tkinter as tk

#create a window
root = tk.Tk()

#size of the window(width*height)
width,height=400,400



root.title("Hello World")#title of the window
root.iconbitmap("icon.ico")  # Ensure you have an icon file named 'icon.ico'
#resize the window-when you give false it cannot be resizable
root.resizable(width=True, height=True) 

#rotate to the middle of the window
display_width=root.winfo_screenwidth()
display_height=root.winfo_screenheight()
left=int(display_width//2 - width/2)
top=int(display_height//2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}')


#run the window
root.mainloop()

#basic widgets
