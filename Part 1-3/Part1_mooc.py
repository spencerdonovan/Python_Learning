# -*- coding: utf-8 -*-
"""
MOOC Part 1

Created on Tue Jul 16 14:52:57 2024

@author: Charles.Donovan
"""

# %%                                    ******* Conditional statements ********


# %% Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

# Write your solution here
from math import sqrt
year = int(input("Please type in a number:"))
if year == 1984:
    print("Orwell")


# %% Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.

num = int(input("Please type in a number:"))
if num < 0:
    num = num*(-1)
print(f"The absolute value of this number is {num}")

# %% Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

name = input("Please tell me your name:")
if name != "Jerry":
    soup = int(input("How many portions of soup?"))
    total = soup * 5.9
    print(f"The total cost is {total}")
print("Next Please!")

# %% Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

num = int(input("Please type in a number:"))
if num < 1000:
    print(f"This number is smaller than 1000")
    if num < 100:
        print(f"This number is smaller than 100")
        if num < 10:
            print(f"This number is smaller than 10")
print("Thank you!")

# %% Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

num_1 = int(input("Number 1:"))
num_2 = int(input("Number 2:"))
operation = input("Operation:")
if operation == "add":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
if operation == "multiply":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
if operation == "subtract":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")

# %% Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

temp_F = int(input("Pleas type in a temperature (F):"))
temp_C = (temp_F-32)*(5/9)
print(f"{temp_F} degrees Fahrenheit equals {temp_C} degrees Celsius")
if temp_C < 0:
    print("Brr! It's cold in here!")

# %% Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
DOW = input("Day of the week:")
pay = wage * hours

if DOW == "Sunday":
    pay *= 2

print(f"Daily wages: {pay} euros")

# or my clunky way below..

wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
DOW = input("Day of the week:")
pay = wage * hours
pay_p = wage*2*hours
if DOW == "Sunday":
    print(f"Daily wages: {pay_p} euros")
else:
    print(f"Daily wages: {pay} euros")


# %% Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

#   x = (-b ± sqrt(b²-4ac))/(2a).

#    You can assume the equation will always have two real roots, so the above formula will always work.


# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5


a = float(input("What is the value of a: "))
b = float(input("What is the value of b: "))
c = float(input("what is the value of c: "))

d = (b**2) - (4*a*c)
x_1 = (-b + sqrt(d))/(2*a)
x_2 = (-b - sqrt(d))/(2*a)

s_1 = a*x_1**2 + b*x_1 + c
s_2 = a*x_2**2 + b*x_2 + c

print(f"the roots are {x_1} and {x_2}")
