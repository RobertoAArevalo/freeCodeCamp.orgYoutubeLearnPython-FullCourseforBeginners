# Lesson 25 - Try Except
# This will have program try a piece of code. Everything in the try: section is going to be ran.


try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

#Having 2 excepts allow the program to state what the particular issue was.
# The division error van be stored as a variable err
# best practice in python is to store specific errors like ZeroDivisionError.





