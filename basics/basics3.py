def get_name(fname, sname):
    out_message = "Hi %s %s" % (fname.title(), sname.title())
    return out_message
    
user_fname = input("What is your first name? ")
user_sname = input("What is your second name? ")

print(get_name(user_fname, user_sname))