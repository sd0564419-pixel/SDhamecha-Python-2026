#!/usr/bin/env python3

# get inputs from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))

# find the user's age
age = current_year - birth_year

# print name and age using concatenation and newline
print("Hello, " + first_name + " " + last_name + "!\n" + "You are " + str(age) + " years old this year.")

# add 1 to age for next year
age += 1

# print next year's age using an f-string
print(f"In {current_year + 1}, you will be {age} years old.")

#message
print("=====================")
print("Completed by, Shivang")