#Lesson 12 - Functions

# Functions are collection of code that perform a specific task.
# A lot of lines of code that are doing one thing can be placed inside of a function and then call the function to
# complete the task. They also allow for organization.

# there could be an underscore in between sayhi
# The def sayhi(): is sayint all the code that comes after sayhi is going to be inside of the function.
# The code that is going inside of the function has to be indented.

# The code inside of a function is not going to be executed by default. It has to be called on.
# With the Top and Bot

"""
def sayhi():
    print("Hello User")

print("Top")
sayhi()
print("Bottom")
"""
# When executing the previous code, it will yield

"""
Top
Hello User
Bottom
"""

# this is because sayhi() calls the function and then continues down the lines.


#parameters can be inputted to make the function more powerful. It is information given to the function.
# When information is given to the function, it can use the infomration to produce a result.
"""
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")

# this can be used to retrieve 
Hello Mike, you are 35
Hello Steve, you are 70

"""

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age)) # A string can be used in combination with numbers

say_hi("Mike", 35) #numbers here
say_hi("Steve", 70) #numbers here

#strings, numbers, bullions, arrays, or any type of data can be passed into functions and it'll work
#





