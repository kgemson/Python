def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
# effectively replaces writing 'say_whee = my_decorator(say_whee)' after the 'def' statement
def say_whee():
    print("Whee!")

say_whee()