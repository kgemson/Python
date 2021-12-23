from tkinter import *

window = Tk()
window.geometry("400x250")

def convert_kilos():
    kilos_to_convert = float(e1_value.get())
    t_grammes.insert(INSERT,kilos_to_convert * 1000)
    t_pounds.insert(INSERT,kilos_to_convert * 2.20462)
    t_ounces.insert(INSERT,kilos_to_convert * 35.274)

canvas = Canvas(window,width=400,height=20,bg="#20bebe")
canvas.grid(row=0,column=0,columnspan=3)

l1 = Label(window,text="Insert weight in kilos and click button:",pady=8)
l1.grid(row=1,column=0,columnspan=2)

e1_value = StringVar()  #declare variable into which we can pass the text field value
e1 = Entry(window,textvariable=e1_value,width=20)
e1.grid(row=1,column=2)

b1 = Button(window,text="Convert",command=convert_kilos,bg="#ffffff",pady=2)
#b1.pack()
b1.grid(row=2,column=1)

canvas = Canvas(window,width=400,height=20,bg="#20bebe")
canvas.grid(row=3,column=0,columnspan=3)

l2 = Label(window,text="Weight in grammes:",pady=2)
l2.grid(row=4,column=0)
t_grammes=Text(window,height=1,width=20,padx=2,pady=2)
t_grammes.grid(row=4,column=1,columnspan=2)

l3 = Label(window,text="Weight in pounds:",pady=2)
l3.grid(row=5,column=0)
t_pounds=Text(window,height=1,width=20,padx=2,pady=2)
t_pounds.grid(row=5,column=1,columnspan=2)

l4 = Label(window,text="Weight in ounces:",pady=2)
l4.grid(row=6,column=0)
t_ounces=Text(window,height=1,width=20,padx=2,pady=2)
t_ounces.grid(row=6,column=1,columnspan=2)

canvas = Canvas(window,width=400,height=50,bg="#20bebe")
canvas.grid(row=7,column=0,columnspan=3)


window.mainloop()