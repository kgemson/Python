user_input = input("What is your name? ")
message = "Hello %s" % user_input
message = f"Hello {user_input}   "

print(message)

user_fname = input("What is your first name? ")
user_sname = input("What is your second name? ")
#message = "Hello %s %s" % (user_fname,user_sname)
message = f"Hello {user_fname} {user_sname}."

print(message)