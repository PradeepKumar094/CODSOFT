import tkinter as tk
from tkinter import *
import random
import string

pas1 = ""

def GenPass():
    global pas1
    try:
        if entry1.get() and entry2.get():
            le = int(entry2.get())
            l = string.ascii_letters + string.digits + string.punctuation
            pas1 = ''.join(random.choice(l) for i in range(le))
            pas2 = "The Password Generated is :  "+pas1
            label3.config(text=pas2,fg='red')
        elif entry2.get():
            pas1 = "Enter User Name !!"
            label3.config(text=pas1,fg='red')
        else:
            pas1 = "Enter Desired length of password !!"
            label3.config(text=pas1,fg='red')            
    except ValueError:
        print("Please enter a valid integer for the password length.")
        
def ResetPass():
    entry1.delete(0,END)
    entry2.delete(0,END)
    label3.config(text="")
    label4.config(text="")

def AcceptPass():
    global pas1
    s = "Hello "+entry1.get()+"! your password is :  "+pas1
    label4.config(text=s)

window = tk.Tk()
window.geometry('500x500')
window.configure(bg='light blue')

label1 = tk.Label(window,text="PASSWORD GENERATOR",font=("Times New Roman",40,"bold"),fg="black",bg='light blue')
label1.place(x=450,y=4)

label2 = tk.Label(window,text="Enter  User  Name  : ",font=("Times New Roman",25),fg="black",bg='light blue')
label2.place(x=350,y=150)

entry1 = tk.Entry(window,font=('Times New Roman',23))
entry1.place(x=680,y=155)

label2 = tk.Label(window,text= "Enter  the  desired  length  of  the  password  :",font=("Times New Roman",25),bg='light blue')
label2.place(x=200,y=250)
    
entry2 = tk.Entry(window,font=('Times New Roman',20))
entry2.place(x=930,y=260)

button1 = tk.Button(window,text="GeneratePassword",font=('Times New Roman',20,"bold"),bg='yellow',command=GenPass)
button1.place(x=300,y=400)

button2 = tk.Button(window,text="AcceptPassword",font=('Times New Roman',20,"bold"),bg='gold',command=AcceptPass)
button2.place(x=640,y=400)

button3 = tk.Button(window,text=" ResetPassword ",font=('Times New Roman',20,"bold"),bg='cyan',command=ResetPass)
button3.place(x=950,y=400)

label3 = tk.Label(window,font=("Times New Roman",25,"bold"),bg='light blue')
label3.place(x=300,y=550)

label4 = tk.Label(window,font=("Times New Roman",25,"bold"),bg='light blue')
label4.place(x=300,y=650)

window.mainloop()
