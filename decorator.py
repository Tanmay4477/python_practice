def upper_case(def_func):
    def wrapper(value):
        upper_value = value.upper()
        def_func(upper_value)
    return wrapper
    
@upper_case
def take_input(value):
    print(value)

# take_input("something")


def print_message(func_def):
    def wrapper():
        print("Function is being called!")
        func_def()
    return wrapper

@print_message
def lets_print():
    print("Hello World")

lets_print()