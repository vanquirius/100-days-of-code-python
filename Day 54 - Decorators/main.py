# coding=utf-8
# Marcelo Ambrosio de Goes
# marcelogoes@gmail.com
# 2022-04-10

# 100 Days of Code: The Complete Python Pro Bootcamp for 2022
# Day 54 - Decorators

import time


def speed_calc_decorator(input_function):
    def wrapper_function():
        start_time = time.time()
        print("Start time: " + str(start_time))
        input_function()
        end_time = time.time()
        print("End time: " + str(end_time))
        run_time = end_time - start_time
        print("Total run time was: " + str(run_time) + "s")
        print("")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
    print("Fast function done.")

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
    print("Slow function done.")

fast_function()
slow_function()