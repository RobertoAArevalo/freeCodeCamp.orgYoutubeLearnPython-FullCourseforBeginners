#Lesson 15 - If Statments & Comparisons

# Creating a python funciton to give the biggest number it is given.
# There will be 3 parameters of input and it will print out the biggest number.
# An if statement is used to determine which number is the largest


def max_num(num1, num2, num3): # A function with 3 parameters.
    if num1 >= num2 and num1 >= num3: # 1st Para. These numbers are being compared here. This is kinda of like a True or false statement or a bullion.
        return num1
    elif num2 >= num1 and num2 >= num3: # 2nd Para. These numbers are being compared and will end up being a true or false value.
        return num2
    else:                                 # 3rd Para.
        return num3

print(max_num(300,40,5))

# returs 300

"""
def max_num(num1, num2, num3):
    if "dog" == "dog" and num1 >= num3: #string example 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(300,40,5))
"""

# if num1 == num2 is a way to see if 2 things equal each other
# if num1 != num2 is a way to say not equal to
# >, <, <=, >= are other operators to compare different values

# This is a good way to compare. We can compare numbers or strings.



