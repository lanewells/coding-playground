# Exercise 1: Character input

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old.

# Solution:

import datetime

# name = input("What is your name?")
# age = int(input("How old are you?"))
# current_year = datetime.datetime.now().year
# year = (100 - age) + current_year

# print(f'{name}, in the year {year} you will be 100 years old.')
# => Lane, in the year 2097 you will be 100 years old.



# Exercise 2: Odd or even

# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Solution:

# num = input("Give me a number: ")
# remainder = int(num) % 2
# if remainder == 1:
#     result = 'odd'
# elif remainder == 0:
#     result = 'even'
# print('Your number (' + str(num) + ') is an ' + result + ' number.')



# Exercise 3: List less than ten

# Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Solution:

# # basic
# for x in a:
#     if x < 5:
#         print(x)

# # return in new list
# new_list = []

# for x in a:
#     if x < 5:
#         new_list.append(x)
# print(new_list)

# # one line code
# print([x for x in a if x < 5])



# Exercise 4: Divisors

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Solution: 

num = int(input("Give me a number: "))
a = range(1, num)
new_list = [x for x in a if num % x == 0]
print(new_list)

# refactored and accounting for number itself as a divisor:
num = int(input("Give me a number: "))
new_list = print([x for x in range(1, num + 1) if num % x == 0])

