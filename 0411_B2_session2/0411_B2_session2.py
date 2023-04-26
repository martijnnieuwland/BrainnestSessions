# 1.Rewrite your pay computation with times-and-a-half for overtimes and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
def computepay(*args):
    try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
    except:
        ValueError(print("Sorry only numbers please."))
    
    try:
        if hours <= 40:
            pay = hours * rate
        elif hours > 40:
            pay = 40 * rate + (hours - 40) * (1.5 * rate)
        return(f"Pay: {pay}")
    except:
        NameError(print("Without proper input we cannot calculate your pay."))

# pay = computepay()
# print(pay)


# 2.2.Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
def computergrade(*score):
    score = float(input("Hello, between the range 0.0 and 1.0 what's the score?:  "))

    try:
        if score < 0.0 or score > 1.0:
            print("Please enter a score between the specified range 0.0 - 1.0.")
        elif score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        elif score < 0.6:
            grade = "F"
        return(f"Your grade is: {grade}!")
    except:
        NameError(print("We cannot calculate your grade with this input."))

grade = computergrade()
print(grade)


# problem
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
def greeting(*times):
    for time in times:
        print(f"Good {time}!")
        feeling = input("How are you feeling? ")
        print(f"I am happy to hear that you are feeling {feeling}.")


# greeting("morning", "afternoon", "evening")


# 1.Write a program which repeatedly reads numbers until the
# user enters `done`. Once `done` is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

# functions to be used:

# from statistics import mean
# sum() - len() - sum()/len() - mean()
def calculate():
    print("Please enter your numbers.  To quit enter 'done'.")
    number = 0
    numbers = []

    while number != "done":
        try:
            number = input("Enter a number: ")
            numbers.append(int(number))
        except:
            if number != "done":
                ValueError(print("Invalid input"))
    return(f"{sum(numbers)} {len(numbers)} {sum(numbers)/len(numbers)}")
