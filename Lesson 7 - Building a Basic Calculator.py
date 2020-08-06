#Lesson 7 - Building a Basic Calculator

#Get 2 numbers from a user and then add the 2 numbers to get the sum.
# Python always puts things into a string.
# To create the num1 and num2 variables into numbers, the strings that are inputted by the user
# will have to be converted into numbers.

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = num1 + num2
#print(result)
    #The following will only add the 2 variables as strings but not add them together.

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1) + int(num2) # adding int() will convert these into numbers
# This int() will look for an integer, so decimals will not work with it.

#print(result)



num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) #float will allow for both integers and decimals.

print(result)

# 2 variables were created and 2 numbers were inputted by users and stored in these variables.
# The responses were converted into numbers and they were added together and printed them out.

