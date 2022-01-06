from tkinter import *
#import backend_sqlite as be
from backend_postgre_oop import Database

dbconn="dbname='mydb' user='postgres' password='budape5t' host='localhost' port='5432'"
db=Database(dbconn) # instantiate Database class which invokes constructor. Note, 'self' is automatically passed as first parm.

#################################################################################################################################
# Define functions to link frontend to backend
# each function below executes command for one of the buttons
#################################################################################################################################

def view_command():
    list1.delete(0,END)
    for r in db.view_all():
        list1.insert(END,r) # the END parameter is required to insert a positional parameter to say where new row is to go.
                            # Can be a positional integer, but END means just add to end of list

def search_command():
    list1.delete(0,END)
    rows_found=db.search_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #'get' required because 'StringVar' != String
    if len(rows_found)==0:
        list1.insert(0, '*** No matching rows found ***') 
    else:
        for r in rows_found:
            list1.insert(END,r) # the END parameter is required to insert a positional parameter to say where new row is to go.

def add_command():
    db.add_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #'get' required because 'StringVar' != String
    display_listbox_message('Entry successfully added to database:')
    clear_entry_fields()

def update_command():
    #my_id=get_selected_row()[0] : this doesn't work as we need 'event' parameter to call function
    my_id=selected_tuple[0]
    db.update_entry(my_id,title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) #'get' required because 'StringVar' != String
    display_listbox_message('Record successfully updated in database')
    clear_entry_fields()

def delete_command():
    #my_id=get_selected_row()[0] : this doesn't work as we need 'event' parameter to call function
    my_id=selected_tuple[0]
    db.delete_entry(my_id)
    display_listbox_message('Entry successfully deleted from database')
    clear_entry_fields()

def close_command():
    window.destroy()

###################################################################################
# functions below execute additional steps required for the above functions to work

def get_selected_row(event):
    # function is called when we bind the listbox to this method.
    # Global variable is required as we cannot call this function from delete/update functions 
    # without an 'event' parameter - we need to declare global variable and just use that. Hence no 'return'.
    # 'try' element removes bugs, e.g. getting 'index out of bounds' when you click on a component
    try:
        index=list1.curselection()[0]
        global selected_tuple   
        selected_tuple=list1.get(index)

        # update text boxes with selected values
        clear_entry_fields()
        e1.insert(0,selected_tuple[1])
        e2.insert(0,selected_tuple[2])
        e3.insert(0,selected_tuple[3])
        e4.insert(0,selected_tuple[4])
    except IndexError:
        pass
#    return selected_tuple - don't need since we are now using global variable

def clear_entry_fields():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def display_listbox_message(message):
    list1.delete(0,END)
    list1.insert(0, message)

#################################################################################################################################
# Set up GUI and add components
#################################################################################################################################

window=Tk()
window.wm_title("Bookstore")

# Add labels
l1=Label(window,text="Title",padx=5)
l1.grid(row=0,column=0)

l2=Label(window,text="Author",padx=5)
l2.grid(row=0,column=2)

l3=Label(window,text="Year",padx=5)
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN",padx=5)
l4.grid(row=1,column=2)

l5=Label(window,height=2)
l5.grid(row=8,column=0,columnspan=3)

# Add entry fields next to labels
title_text = StringVar()
e1=Entry(window,textvariable=title_text,border=3)
e1.grid(row=0,column=1)

author_text = StringVar()
e2=Entry(window,textvariable=author_text,border=3)
e2.grid(row=0,column=3)

year_text = StringVar()
e3=Entry(window,textvariable=year_text,border=3)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4=Entry(window,textvariable=isbn_text,border=3)
e4.grid(row=1,column=3)

# Add listbox to display output
list1=Listbox(window,width=35)
list1.grid(row=2,column=0,columnspan=2,rowspan=6)

list1.bind('<<ListboxSelect>>',get_selected_row) # required to link an event to the function

# define scrollbar 
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# configure to work with Listbox
list1.configure(yscrollcommand=sb1)
sb1.configure(command=list1.yview)

# Define buttons on right
# Add commands to link functionality to backend script
b1=Button(window,text="View all",width=12,padx=5,pady=2,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry",width=12,padx=5,pady=2,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry",width=12,padx=5,pady=2,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,padx=5,pady=2,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,padx=5,pady=2,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,padx=5,pady=2,command=close_command)
b6.grid(row=7,column=3)

# mainloop
window.mainloop()