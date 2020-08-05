#Lesson 4 Working With Strings

#Strings are plain text.
# To create a string there needs to be quotation marks around the plain text.
# Inserting a \n in between words will create a break in the code.
# Inserting a \" will tell Python to print the quotation mark. Any \x will print the x.
# A \  alone will print a backslash.
# Phrase can be used to assign a text. Once print(phrase) is used, it will print the assigned text.
# Concatenation can also be used. Concatenation is the process of taking a string and appending another string onto it.
# A function is a small block of code that can be ran that will perform a specific operation.
# Functions can be used to modify strings and to get information about strings.

 # phrase.upper will make all of the phrase in upper case
#phrase.isupper() will report back a true or false value. if the whole string is true, it will report back true.
# These functions can be used in combination with each other.
# using the functions phrase.upper() will turn everything upper case and adding .isupper() will report back as true
    #because everything has been converted into upper.

#The length of the string in characters can be derived by using (len(phrase))
# Individual characters can also be determined by using (phrase[0]) for the first character in the string.
    #this feature will be useful

# An index function will say where specific character or string is located.
# print(phrase.index("")) when a value is given in between these parenthesis or when a parameter is passed it will return
# an index back with the location of the given character
# This can also be used for whole words.
# If I placed a letter or word in the parenthesis that is not in the string, it will report back as an error.

# print(phrase.replace("Giraffe", "Elephant")) will replace giraffe with elephant and this function can replace letters
# too.


phrase = "Giraffe Academy"
print(phrase.replace("Giraffe", "Elephant"))

# The functions covered in this lesson were some of the most common functions used for string in Python.
# functions and strings are used a lot in Python.