#Lesson 23 - Build a Translator

"""
Giraffe Language
vowels -> g
---------

dog -> dgg
cat -> cgt
"""
""""
def translate(phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou": OR # in python we can check is something is part of something else
         if letter.lower() in "aeiou":
             if letter.isupper():
                 translation = translation + "G"
             else:
                 translation = translation + "g" # This is to convert vowel into a g


        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
"""

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
        return translation


print(translate(input("Enter a phrase: ")))

#those not result the way it should
# Enter a phrase: asdfasdfasdfasdf
# g
#
# Process finished with exit code 0










# Running a for loop in combination with a if statement which is a powerful structure.

# results Enter a phrase: dog
# dgg
#
# Process finished with exit code 0

# results Enter a phrase: To be or not to be
# Tg bg gr ngt tg bg
#
# Process finished with exit code 0




