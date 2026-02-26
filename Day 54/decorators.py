import time

def delay_decorator(function):
    """
    A decorator is a function that wraps another
     function to add extra behavior
     without changing the original function's code.
    """
    def wrapper_function():
        #add some functionality before starting program
        time.sleep(2)
        function()
        #add some functionality after completion of program
    return wrapper_function()


@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

def say_greetings():
    print("how are you ?")

