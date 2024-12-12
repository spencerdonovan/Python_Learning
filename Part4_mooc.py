# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:58:32 2024

MOOC Part 4

@author: Charles.Donovan
"""
import pandas as pd
from docx import Document

# %% =============================================================================
# *********************** Visual Studio Code **********************************
# =============================================================================

# Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.

while True:
    string = input("Editor:")

    if string.lower() == "word" or string.lower() == 'notepad':
        print("awful")
    elif string.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")

# %% Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. If the second argument is an empty string, the line should consist of stars.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


line(3, "PIZZA")

# %%Please write a function named box_of_hashes, which prints out a rectangle of hash characters. The function takes one argument, which specifies the height of the rectangle. The rectangle should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in your line function.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


def box_of_hashes(height):
    i = 1
    while i <= height:
        line(10, "#")
        i += 1

# %% Please write a function named square_of_hashes, which draws a square of hash characters. The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


def square_of_hashes(height):
    i = 1
    while i <= height:
        line(height, "#")
        i += 1

# %% Please write a function named square, which prints out a square of characters, and takes two arguments. The first parameter specifies the length of the side of the square. The second parameter specifies the character used to draw the square.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


def square(length, char):
    i = 1
    while i <= length:
        line(length, char)
        i += 1

# %% Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


def triangle(length, char):
    i = 1
    k = length
    while i <= k:
        line(i, char)
        i += 1

# %%Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, while the third parameter specifies its height. The fourth parameter specifies the filler character of the rectangle. The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.


def line(num, string):
    if string == "":
        string = "*"
    print(num*string[0])


def shape(length, char, height, char_2):
    i = 1
    k = length
    j = height
    while i <= k:
        line(i, char)
        i += 1
    while j >= 1:
        line(length, char_2)
        j -= 1


# %% *************** USING RETURN VALUES FROM FUNCTIONS *******************

# Please write a function named greatest_number, which takes three arguments. The function returns the greatest in value of the three.

def greatest_number(num1, num2, num3):
    list1 = []
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)

    return max(list1)


# %% Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.


def same_chars(text, int1, int2):
    if int1 >= len(text) or int2 >= len(text):
        return False
    return text[int1] == text[int2]


# %% Please write three functions: first_word, second_word and last_word. Each function takes a string argument.

# As their names imply, the functions return either the first, the second or the last word in the sentence they receive as their string argument.

# In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space character. There will be no spaces in the beginning or at the end of the argument strings.

def first_word(text):
    words = text.split(" ")
    return words[0]


def second_word(text):
    words = text.split(" ")
    return words[1]


def last_word(text):
    words = text.split(" ")
    return words[-1]
