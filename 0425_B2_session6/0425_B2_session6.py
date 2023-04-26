# 1. A decorator that repeats a function call a specified number of times

def my_function():
    return "Hello, world!\n"
    
    
def thrice(func):
    return func() * 3
    
    
print(thrice(my_function))


"""Create a decorator my_logger that logs the name of the function being called and the arguments it was called with. 
The logger should output the function name and arguments to the console each time the function is called."""

def my_function(x, y):
    return x, y

def my_logger(func):
    input = func(2, 3)
    return f"Calling function {func.__name__} with args {input} and kwargs {{}}"

print(my_logger(my_function))


"""Find the average value of a specific key in a JSON file containing an array of dictionaries:
Write a Python program that reads a JSON file containing an array of dictionaries, 
calculates the average value of a specific key across all dictionaries in the array, and prints the result. 
For example, given the following JSON file named data.json"""

import json

with open("Sessions/0425_B2_session6/data.json", "r") as j:
    data = json.load(j)
    total = 0
    for person in data:
        total += person['score']
    average = total / len(data)

print(average)
    

"""Write a Python program that reads a JSON file containing a list of numbers, finds the maximum and minimum values, and prints them to the console."""

import json

with open("Sessions/0425_B2_session6/number.json", "r") as n:
    numbers = json.load(n)
    
    print(max(numbers), min(numbers))
