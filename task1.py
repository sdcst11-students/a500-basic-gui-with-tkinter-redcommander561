import tkinter as tk
from tkinter import *
from tkinter import ttk


#Create the user interface described in the image task1.png.
#You should use only the .pack() or .grid() methods
#(2 points) 

window = tk.Tk()
window.title("tk")
window.geometry("450x20")

entry1 = tk.Entry(window, width= 15)
entry2 = tk.Entry(window, width= 15)
label1 = tk.Label(window, text="x", width=5)
label2 = tk.Label(window, text="=",width=3)
entry2 = tk.Entry(window,width=15)
entry3 = tk.Entry(window,width=25)



entry1.grid(row=1,column=1)
label1.grid(row=1,column=2)
entry2.grid(row=1,column=3)
label2.grid(row=1,column=4)
entry3.grid(row=1,column=5)
window.mainloop()