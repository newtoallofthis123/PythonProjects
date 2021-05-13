# Name of the Project : cal-cli.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : None

''' The following is registered under the MIT License, NoobScience 2021. You are free to use it
as you like as long as you know what you are doing.
Enjoy using and check some of my other projects at https://github.com/newtoallofthis123'''

# Don't Change the code after this line unless you know what you are doing.

#! /usr/bin/env python3

'''
A simple cli tool written in python to be used as a calculator.
By NoobScience. To use it,
just switch to the directory you stored it in and open the terminal there and
type python alarm.py
Available for Windows, Mac, Linux and written in python'''

# Getting the user imput about the two numbers and operation
print("Cal-cli by NoobScience")
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second Number "))
operator= input("Enter the operator ")

# Defining operators and printing the operated numbers
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Unknown, please try again")

# Enjoy

    
    
