# -*- coding: utf-8 -*-
"""
MOOC Part 2

Created on Tue Jul 23 15:11:48 2024

@author: Charles.Donovan

"""

# %% ****************** PROGRAMMING TERMINOLOGY ****************

# The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.

  number = input("Please type in a number: ")
  if number > 100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
      print("Its value is now" + number)
 print(number + " must be my lucky number!")
 print("Have a nice day!)
# %%

number = int(input("Please type in a number: "))
if number>100:
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", + number)
print(number, " must be my lucky number!")
print("Have a nice day!")

# %%  Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

word = input("Please type in a word:")
if len(word) > 1:
    print(f"There are {len(word)} letter in the word {word}")
print("Thank you!")

# %% Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

num = float(input("Please type in a number:"))
integer = int(num)
decimal = num-integer
print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")

# %%    ********************* MORE CONDITIONALS *****************

# Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

age = int(input("How old are you? "))
if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")
    
# %%  Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

num_1 = int(input("Please type in the first number:"))
num_2 = int(input("Please type in another number:"))

if num_1 > num_2:
    print(f"The greater number was: {num_1}")
elif num_2 > num_1:
    print(f"The greater number was: {num_2}")
elif num_2 == num_1:
    print("The numbers are equal!")

# %%  Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

print("Person 1:")
name_1 = input("Name:")
age_1 = int(input("Age:"))
print("Person 2:")
name_2 = input("Name:")
age_2 = int(input("Age:"))

if age_1 > age_2:
    print(f"The elder is {name_1}")
elif age_1 < age_2:
    print(f"The elder is {name_2}")
else:
    print(f"{name_1} and {name_2} are the same age")

# %% Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

# the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# only the standard English alphabet of a to z, or A to Z, is used.
# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

word_1 = input("Please type in the 1st word:")
word_2 = input("Please type in the 2nd word:")

if word_1 > word_2:
    print(f"{word_1} comes alphabetically last.")
elif word_1 < word_2:
    print(f"{word_2} comes alphabetically last.")
elif word_1 == word_2:
    print("You gave the same word twice.")


# %% *************************** COMBINING CONDITIONALS *******************************

# Please write a program which asks for the user's age. If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

age = int(input("What is your age?"))

if 0 <= age < 5:
    print("I suspect you can't write quite yet")
elif age < 0:
    print("That must be a mistake")
elif age >= 5:
    print(f"Ok, you're {age} years old")


# %%  Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

name = input("Please type in your name:")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")


# %% The table below outlines the grade boundaries on a certain university course. Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points = int(input("How many points [0-100]: "))
 
if points < 0 or points > 100:
    grade = "impossible!"
elif points < 50:
    grade = "fail"
elif points < 60:
    grade = "1"
elif points < 70:
    grade = "2"
elif points < 80:
    grade = "3"
elif points < 90:
    grade = "4"
else:
    grade = "5"
 
print(f"Grade: {grade}")

# %%  Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

number = int(input("Number: "))
 
if number % 3 == 0 and number % 5 == 0:
    # This condition must be evaluated first, because if this is true,
    # also both of the following conditions are true
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

# %% Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

year = int(input("Please type in a year:"))

if year < 100 and year % 4 == 0:
    print("That year is a leap year")
elif year > 99 and year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("That year is a leap year")
elif year > 99 and year % 4 == 0 and year % 100 != 0:
        print("That year is a leap year")
else:
    print("That year is not a leap year")
    
year = int(input("Please type in a year: "))
 
# First, we make assumption that a year is not a leap year
leap_year = False
 
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
elif year % 4 == 0:
    leap_year = True
 
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")


# %% Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

L1 = input("1st letter:")
L2 = input("2nd letter:")
L3 = input("3rd Letter:")

if L1 > L2 > L3 or L1 < L2 < L3:
    middle = L2
elif L2 > L1 > L3 or L2 < L1 < L3:
    middle = L1
elif L2 > L3 > L1 or L1 > L3 > L2:
    middle = L3
print(f"The letter in the middle is {middle}")

# %% Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.

G = int(input("Value of gift:"))

if G < 5000:
    tax = 0
elif 5000 <= G <25000:
    tax = (100+(G-5000)*0.08)
elif 25000 <= G < 55000:
    tax = (1700+(G-25000)*0.10)
elif 55000 <= G < 200000:
    tax = (4700+(G-55000)*.12)
elif 200000 <= G < 1000000:
    tax = (22100+(G-200000)*0.15)
elif 1000000 <= G:
    tax = (142100+(G-1000000)*0.17)

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")


# %%  ************************** SIMPLE LOOPS *******************************
# Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

while True:
    print("hi")
    ans = input("Shall we continue?")
    if ans == "no":
        break
print("okay then")

# %% Please write a program which asks the user for integer numbers.

# If the number is below zero, the program should print out the message "Invalid number".

# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.

# In either case, the program should then ask for another number.

# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

from math import sqrt

while True:
    num = int(input("Please type in a number:"))
    if num < 0:
        print("Invalid number")
    elif num > 0:
        print(f"{sqrt(num)}")
    elif num == 0:
        break
print("Exiting...")

# Solution

while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number > 0:
        print(sqrt(number))
    else:
        print("Invalid number")
        
print("Exiting...")

# %% This program should print out a countdown.

print("Countdown!")
number = 5
while True:
  print(number)
  number = number - 1
  if number == 0:
    break
print("Now!")

# %% Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

pass1 = input("Password:")
while True:
    pass2 = input("Repeat password:")
    if pass2 != pass1:
        print("They do not match!")
    if pass2 == pass1:
        break
print("User account created!")

# %% Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

# If the user gets it right on the first try, the program should print out something a bit different:

correct = 4321
count = 0

while True:
    count += 1
    pin = int(input("PIN:"))
    if pin != correct:
        print("Wrong")
    if pin == correct:
        break

if count == 1:
    print ("Correct! It only took you one single attempt!")
else:
    print (f"Correct! It took you {count} attempts")

# mooc sol

attempts = 1
while True:
    pin = input("PIN: ")
    if pin == "4321":
        break
    print("Wrong")
    attempts += 1
 
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")


# %% Please write a program which asks the user for a year, and prints out the next leap year.

# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

year = int(input("Year:"))

next_year = year+1

while True:
    if next_year % 4 == 0 and next_year % 100 != 0 or next_year % 400 == 0:
        break
    next_year += 1
print(f"The next leap year after {year} is {next_year}")


# %% Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

# Change the program so that the loop ends also if the user types in the same word twice in a row.

words = ""
word_2 = ""

while True:
    word = input("Please type in a word:")
    if word == "end" or word == word_2:
        break
    words += word + " "
    word_2 = word
print(words)

# %% Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end should not be included in the count.

# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

# The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

# The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

nums = 0
sums = 0
neg = 0
pos = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    nums += 1
    sums += num
    mean = sums/nums
    if num > 0:
        num = pos
        pos += 1
    if num < 0:
        num = neg
        neg += 1


print(f"Numbers typed in {nums}")
print(f"The sum of the numbers is {sums}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")



