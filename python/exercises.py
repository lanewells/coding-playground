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

# num = int(input("Give me a number: "))
# a = range(1, num)
# new_list = [x for x in a if num % x == 0]
# print(new_list)

# # refactored and accounting for number itself as a divisor:
# num = int(input("Give me a number: "))
# new_list = print([x for x in range(1, num + 1) if num % x == 0])



# Exercise 5: List overlap

# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are 
# common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Solution:

# new_list = []
# for x in a:
#     if x in b and x not in new_list:
#         new_list.append(x)
# print(new_list)

# new_list = []
# print([x for x in a if x in b])
# print(new_list)

# new_list = []
# print([x for x in a if x in b and x not in new_list])

# new_list = list(set(a) & set(b))
# print(new_list)

# print(list(set(a) & set(b)))



# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# Solution:

s = input("Type a string of characters: ")
for i in range(len(s) // 2):
    if s[i] != s[-i-1]:
        print("not palindrome")
        break
else: print("palindrome!")



# Exercise 7 (and Solution)
# Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# Solution:

# new_list = [x for x in a if x % 2 == 0]
# print(new_list)