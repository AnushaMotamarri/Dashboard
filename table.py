from Tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="")
        b.grid(row=i, column=j)
        frame1=Frame(root)
        frame1.grid(row=i, column=j)
        l = Label(frame1,text = "abc")
        l.grid(row=0, column=1)
        b1=Label(frame1,text="3")
        b1.grid(row=1,column=1)
mainloop()
