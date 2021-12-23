from tkinter import *

window = Tk()

def km_to_miles():
    km = float(e1_value.get()) * 1.6
    t1.insert(END,km)

b1 = Button(window,text="Execute",command=km_to_miles)
#b1.pack()
b1.grid(row=0,column=0)

e1_value = StringVar()  #declare variable into which we can pass the text filed value
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()