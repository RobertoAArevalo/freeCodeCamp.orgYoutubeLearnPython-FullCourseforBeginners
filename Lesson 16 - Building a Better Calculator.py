# Lesson 16 - Building a Better Calculator

# This calculator will allow a user to add, subtract, multiply, or divide.
# add, subtract, multiply, and divide are all operators

# There will be 3 variables. 1 for the first number, 1 for the second number, and the last one for the operator.
# The values that the user inputs will be stored in the given variables.

# Whatever the user enters will get converted into a number.
# Generally in python when an input is given by a user, it is converted into a string.
# Since we are building a calculator, a number data type instead of a string will be useful.
# The float function will convert the user inputs into a float.
    #This will require the user to have to enter a number or the code will not run.





num1 = float(input("Enter first number: "))
op = input("Enter first number: ") #This should not be a number. It should remain as a string.
num2 = float(input("Enter second number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print ("Invalid operator")

"""
executes too
Enter first number: 17
Enter first number: -
Enter second number: 10
7.0
"""

#Got input from the user and used if statements to do what they wanted to do.
# This checked to see if the user wanted +, -, /, *, or if they entered a non usable operator.
#
