from tkinter import *

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("Game")

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky='news')

label = Label(f1, text="ROCKPAPERCAESAR")
label.grid(column=2, row=0)

e1 = Entry(f1)
e1.grid(column=2, row=1)
e1.insert(0, "Username")

e2 = Entry(f1)
e2.grid(column=2, row=2)
e2.insert(0, "Password")

button = Button(f1, text="Login")
button.grid(column=2, row=3)
button = Button(f1, text="SignUp")
button.grid(column=2, row=5)

raise_frame(f1)
root.mainloop()