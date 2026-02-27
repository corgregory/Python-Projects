"""
Build a Number Pattern Generator
In this lab you will practice the basics of Python by building a small app that creates a number pattern.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named number_pattern that takes a single parameter n (representing a positive integer).
number_pattern should use a for loop.
number_pattern(n) should return a string with all the integers starting from 1 up to n (included) separated by a space. For example, number_pattern(4) should return the string 1 2 3 4.
If the argument passed to the function is not an integer value, the function should return Argument must be an integer value..
If the argument passed to the function is less than 1, the function should return Argument must be an integer greater than 0..
"""
#This project really helped me with my debugging skills.
#I kept running into an issue where the output would print 1 number
#I originally solved this by making a number_list variable 
#but the requirements wanted me to use string concatenation.

def number_pattern(n):
    #number_string will store an interger(n) as string
    number_string = " "
    #these conditional statements will check for valid input.
    if not isinstance(n,int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    #I set my loop up to also include the variable passed in 
    #because by default the range funstion will exclude the (n) value.
    for number in range(1,n+1):
     #I used string concatention with spaces to have spaces between my
     #string of numbers.
        number_string += str(number) + " "
    return number_string.strip()
#here are some test calls to make sure the function is working properly.
print(number_pattern(5))

print(number_pattern(47))

print(number_pattern(50))



