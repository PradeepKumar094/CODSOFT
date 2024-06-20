import tkinter as tk
val = " "
def dis(key):
    global val
    val += key
    label1.config(text = val)

def res():
    global val
    res = ""
    if val != "":
        try:
            res = str(eval(val))
        except:
            res = "Error"
            val = ""
        label1.config(text = res)

def clr():
    global val
    val = ""
    label1.config(text = val,)    
    

window = tk.Tk()
window.title("CALCULATOR")
window.configure(bg='light blue')

label1 = tk.Label(window,width = 30,height=4,font = ("Dosis",20,"bold"),bg='black',fg='white')

label1.grid(row=0,column=0,columnspan=5)



button = [ 'C',' (', ' )', ' /',
           '7', '8', '9',' *',
           '4', '5', '6', '+',
           '1', '2', '3', ' -',
           ' .', '0','%', '=']

row = 1
col = 0

for b in button:
    a = lambda x=b: dis(x) if x not in ['=', 'C'] else res() if x == '=' else clr()
    if b=='C':
        tk.Button(window,text=b,bg='red',padx=25, pady=15,bd=10, font=('Oswald',25), command=a).grid(row=row, column=col)
        col += 1
    elif b=='=':
        tk.Button(window,text=b,bg='blue',padx=25, pady=15,bd=10, font=('Oswald',25), command=a).grid(row=row, column=col)
        col += 1
    else:
        tk.Button(window,text=b,padx=25,bg='green',fg='black',pady=15,bd=10,font=('Oswald', 22), command=a).grid(row=row, column=col)
        col += 1
        if col > 3:
            col = 0
            row += 1

window.mainloop()
