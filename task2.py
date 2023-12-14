#Create the user interface described in the image task2.png.
#This image was created using the .grid() method, but you can
#use .pack() or .place() also
#(5 points)

import tkinter as tk
from tkinter import *



 

window = tk.Tk()
window.geometry("575x200")
window.title("T-Town Veterinary Clinic Database")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Name")
label3 = tk.Label(window, text="Type")
label4 = tk.Label(window, text="Breed")
label5 = tk.Label(window, text="Owner")
label6 = tk.Label(window, text="Birthdate")

label1.grid(row=1,column=1)
label2.grid(row=2,column=1)
label1.grid(row=2,column=3)
label4.grid(row=2,column=5)
label5.grid(row=2,column=7)
label6.grid(row=2,column=7)


window.mainloop()