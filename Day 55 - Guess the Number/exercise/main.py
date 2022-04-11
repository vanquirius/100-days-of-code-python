# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 55 - Guess the Number

# Create the logging_decorator() function 👇
def logging_decorator(input_function):
    def wrapper_function(*args):
        function_name = str(input_function.__name__)
        function_arguments = ""
        j = 0
        for i in args:
            function_arguments += str(i)
            j += 1
            if j < len(args):
                function_arguments += ", "
        function_return = str(input_function(*args))
        print("You called the function " + function_name + "(" + function_arguments + ")")
        print("It returned: " + function_return)
    return wrapper_function

# Use the decorator 👇
@logging_decorator
def fast_function(input_1, input_2):
    for i in range(10000000):
        i * i
    return "fast function return"

@logging_decorator
def slow_function(input_3, input_4):
    for i in range(100000000):
        i * i
    return "slow function return"

fast_function(1, 2)
slow_function(3, 4)