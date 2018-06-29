from tkinter import *

root = Tk()

def hello():
    # print('Hello!')
    t.insert('0.0', 'Hello\n')

b = Button(root, text="Push me", command=hello)
b.grid(row=1, column=1)

t = Text(root)
t.grid(row=1, column=2)





root.mainloop()