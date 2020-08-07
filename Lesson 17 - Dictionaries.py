#Lesson 17 - Dictionaries

# Dictionaries is a special structure in python that allows one to store information in key value pairs.
# When someone creates dictionaires, information can be retrieved by using its key.
# The word would be the key because the word is what is able to be identified inside of a dictionary.
# And a value is an actual defintion.

# A program will be created that will allow for a 3 digit month name into a full month name.
# Jan -> January
#Mar -> March


# First name the dictionary
# Dictionaries are always made with curely brackets.
# Key value pairs will have a key and a corresponding value.
# Just type out the key and then type out the value.
# All keys have to be unique


monthConversions = {
    # Key : Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

#print(monthConversions["Mar"])  #This is where we refer to the key, and the value associated with that key will be given back.
# Result #March

#This is another way to retrieve the value.
# .get can be used to specify a default value that is chosen if the key is not found.

#print(monthConversions.get("Dec"))

#print(monthConversions.get("Luv"))
#retrieves None

# If a key is not correlated to any values inside of the dictionary, I can pass it a default value.
print(monthConversions.get("Luv", "Not a valid Key"))
# returns Not a valid Key

# The keys do not have to be strings. Numbers can also be used, but they also have to be unique.
# These will be used a lot to store different kinds of data.


