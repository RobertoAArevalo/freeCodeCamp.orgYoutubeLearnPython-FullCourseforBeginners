#Lesson 14- If Statements

# If Statements are a Special structure in python to help make programs make decisions.
# Certain code can be executed when certain conditions are true.
# Other code can be executed when other conditions are true.

# If statements are able to respond to if statements that are given.
# Depending on data given to the program it will repond respectively.

"""
I wake up
If I'm hungry
    I eat breakfast

I leave my house
if it's cloudy  # if this condition is true, I will bring an umbrella
    I bring an umbrella
otherwise
    I bring sunglasses # if this condition is false, I will bring sunglasses

Im at a restaurant
if I want meat
    I order a steak
otherwise if I want pasta
"""

# An if statement can have as much code as is wanted inside of it.
# The or operator is able to allow for 2 bulllions to work together.
# the and operator can alsp be used
#elif (elseif) is another function



is_male = True #bullion statement
is_tall = False # 2nd bullion statement

if is_male and is_tall: #using an if statement to check if it is true.
    print("You are a male or tall or both") #When the bullion is True, Anything written heere will be executed, if fault, it will not.
elif is_male and not(is_tall): #elseif
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not a male but are tall")
else: #this allows for adding something that is aside from the only true statements.
    print("You are  not male and not tall ")
#You are a short male


"""
is_male = False #bullion statement
is_tall = False # 2nd bullion statement

if is_male or is_tall:
    print("You are a male or tall or both") 
else: 
    print("You are neither male nor tall")
    
response 
You are neither male nor tall

"""
