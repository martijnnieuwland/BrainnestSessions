"""
1. Write a program that uses input to prompt a user for their name and then welcomes them.
"""
userName = input("Hello, please tell us your name:\n")

print(f"Welcome {userName}!")



"""
2. Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
"""
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
    print(f"Pay: {pay}")
except:
    NameError(print("Without proper input we cannot calculate your pay."))



"""
3. Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
"""
celsius = float(input("What's the temperature in celsius?: "))
fahrenheit = celsius * 1.8 + 32
fahrenheit = round(celsius * 1.8 + 32, 1)

print(f"In fahrenheit that would be {fahrenheit}")



"""4. Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
"""
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
    print(f"Your grade is: {grade}!")
except:
    NameError("We cannot calculate your grade with this input.")
