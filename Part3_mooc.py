# -*- coding: utf-8 -*-
"""
MOOC Part 3

Created on Tue Jul 23 15:11:48 2024

@author: Charles.Donovan

"""

# %% =============================================================================
# *********************** LOOPS WITH CONDITIONS **********************************
# =============================================================================

# Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

even = 0

while even < 30:
    even += 2
    print(even)

# %% The program below has some syntactic issues... that are now fixed

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 1:
    print(number)
    number -= 1
print("Now!")

# %% Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

num = int(input("Upper limit:"))
one = 1

while one < num:
    print(one)
    one += 1

# %% Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.

# The execution of the program finishes when the next number to be printed would be greater than the limit set by the user. No numbers greater than the limit should be printed.

limit = int(input("Upper limit:"))
square = 1

while square <= limit:
    print(square)
    square *= 2

# %% Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).

limit = int(input("Upper limit:"))
square = 1
base = int(input("Base:"))

while square <= limit:
    print(square)
    square *= base

# %% Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user. The program should function as follows

limit = int(input("Limit:"))
num = 1
i = 1
while i < limit:
    num += 1
    i += num
print(i)

# %% Please write a new version of the program in the previous exercise. In addition to the result it should also print out the calculation performed

limit = int(input("Limit:"))
num = 1
i = 1
num_string = "1"
while i < limit:
    num += 1
    num_string += (f" + {num}")
    i += num

print(f"The consecutive sum: {num_string} = {i}")


# %%=============================================================================
# **************************** WORKING WITH STRINGS *******************************************
# =============================================================================

# Please write a program which asks the user for a string and an amount. The program then prints out the string as many times as specified by the amount. The printout should all be on one line, with no extra spaces or symbols added.

string = input("Please type in a string:")
amount = int(input("Please type in an amount:"))

print(f"{string*amount}")

# %% Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

string_1 = input("Please type in string 1:")
string_2 = input("Please type in string 1:")

if len(string_1) > len(string_2):
    print(f"{string_1} is longer")
elif len(string_1) < len(string_2):
    print(f"{string_2} is longer")
elif len(string_1) == len(string_2):
    print("The strings are equally long")

# %% Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

string = input("Please type in a string:")
count = len(string)
while count > 0:
    print(string[count-1])
    count -= 1

# %% Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

string = input("Please type in a string:")

if string[1] == string[len(string)-2]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")

# Indexing backwards toooo

word = input("Please type in a string: ")

# Check also that the word is at least two characters long,
# so that the second and second to last characters exist

if len(word) > 1 and word[1] == word[-2]:
    print("The second and the second to last characters are " + word[1])
else:
    print("The second and the second to last characters are different")

# %% Please write a program which prints out a line of hash characters, the width of which is chosen by the user.

width = int(input("Width:"))

print("#"*width)

# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

width = int(input("Width:"))
height = int(input("Height:"))

count = 1
while count <= height:
    print("#" * width)
    count += 1

# %% Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.


while True:
    string = input("Please type in a string:")
    if len(string) > 0:
        print(string)
        print("-"*len(string))
    if len(string) == 0:
        break

# Model Solution

while True:
    string = input("Please type in a string: ")
    if string == "":
        break
    print(string)
    print(len(string) * "-")

# %% Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

# You may assume the input string is at most 20 characters long.

string = input("Please type in a string:")

stars = 20 - len(string)

print("*"*stars+string)

# %% Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

word = input("Word:")

space_1 = int((28-len(word))/2)
space_2 = 28-len(word)-space_1

print("*"*30)
print("*"+" "*space_1+word+space_2*" "+"*")
print("*"*30)


# %% =============================================================================
# ******************* SUBSTRINGS AND SLICES ******************************
# =============================================================================

input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])

# %% Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

string = input("Please type in a string:")

count = 1

while count <= len(string):
    print(string[0:count])
    count += 1

# %% Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

string = input("Please type in a string:")
count = len(string)

while count >= 0:
    print(string[count:])
    count -= 1

# %% Please write a program which asks the user to input a string. The program then prints out different messages if the string contains any of the vowels a, e or o.

# You may assume the input will be in lowercase entirely. Have a look at the examples below.

string = input("Please type in a string:")

while True:
    if "a" in string:
        print("a found")
    else:
        print("a not found")
    if "e" in string:
        print("e found")
    else:
        print("e not found")
    if "o" in string:
        print("o found")
    else:
        print("o not found")
    break

# Model Solution... = better

string = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

# %% Please write a program which asks the user to type in a string and a single character. The program then prints the first three character slice which begins with the character specified by the user. You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

string = input("Please type in a word:")
char = input("Please type in a character:")

while True:
    if char in string:
        x = string.find(char)
    else:
        break
    if x <= len(string)-3:
        print(f"{string[x:x+3]}")
    break

# Or without loop

string = input("Please type in a word:")
char = input("Please type in a character:")

x = string.find(char)
if x != -1 and x < len(string)-2:
    print(string[x:x+3])

# %% Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

string = input("Please type in a word:")
char = input("Please type in a character:")

while True:
    x = string.find(char)
    if x != -1 and x < len(string)-2:
        print(string[x:x+3])
        string = string[x+1:]
    else:
        break

# Better model sol...
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1


# %% Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)

if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " +
          str(index1+len(substring)+index2) + ".")


# %% =============================================================================
# ***************************** MORE LOOPS!! ***************************************
# =============================================================================

# Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

number = int(input("Please type in a number:"))
i = 0

while i < number:
    j = 1
    i += 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j += 1

# %% Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

string = input("Please type in a sentance:")

i = 0
print(string[0])
while i < len(string):
    if string[i] == " ":
        print(string[i+1])
    i += 1

# %% Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

# The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

while True:
    i = 1
    j = 1
    num = int(input("Please type in a number:"))
    if num <= 0:
        print("Thanks and bye!")
        break
    while i <= num:
        j = j * i
        i += 1
    print(f"The factorial of the number {num} is {j}")


# %% Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

num = int(input("Please type in a number:"))

i = 1
j = 2

if num % 2 == 0:
    while i < num:
        print(j)
        print(i)
        i += 2
        j += 2
if num % 2 != 0:
    while i <= num:
        if j < num:
            print(j)
        print(i)
        i += 2
        j += 2

# Model Solution

number = int(input("Please type in a number: "))

index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2

if index <= number:
    print(index)

# %% Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

num = int(input("Please type in a number:"))
i = 1

while i <= num:
    print(i)
    if num > i:
        print(num)
    i += 1
    num -= 1


# %%=============================================================================
# **************************** DEFINING FUNCTIONS ******************************
# =============================================================================

# Write your main function within a block like this:
if __name__ == "__main__":
    greet()

# %% Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order, as in the example below. See the similarly named exercise in part 1 for more details about the brothers.


def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")


seven_brothers()

# %% The exercise contains the outline of the function first_character. Please complete it so that it prints out the first character of the string it takes as its argument.


def first_character(text):
    print(text[0])


# testing the function:
first_character('python')
first_character('yellow')
first_character('tomorrow')
first_character('heliotrope')
first_character('open')
first_character('night')

# %% Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.


def mean(num_1, num_2, num_3):
    print((num_1+num_2+num_3)/3)

# Model Solution


def mean(number1, number2, number3):
    answer = (number1 + number2 + number3) / 3
    print(answer)


mean(1, 2, 3)


# %% Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

def print_many_times(text, times):
    i = 0
    while True:
        if i >= times:
            break
        print(text)
        i += 1

# Model Solution


def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1


print_many_times("poop", 5)

# %% Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.


def hash_square(length):
    square = 0
    while square < length:
        print("#"*length)
        square += 1


hash_square(4)

# %% Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:


def chessboard(square):
    i = 1
    k = 1
    while k <= square:
        j = 1
        print()
        while j <= square:
            print(i, end='')
            if i == 1:
                i = i-1
            elif i == 0:
                i = i+1
            j += 1
        if j % 2 == 1:
            if i == 1:
                i = 0
            elif i == 0:
                i = 1
        k += 1

# Model Solution "SO MUCH NICER :("


def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1

# %% Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.


def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)
