#Lesson 9 - Lists

#There may be large amounts of data when using Python
# A list is just a structure to store lists of information.
# A list usually has many related values in it.
# When creating a normal value it is typically only one value. In this case there are 3.
#There are 3 strings in this list.
#Each elements inside this list have an index. Indices start at 0.
# We can also access indices in the reverse order by using a negative value like -1 which would retrieve Jim.
#If a 1: is used it will retrieve all indeces starting with 1 and values after it.
# If 1:3 is used it will yield Karen, and Jim but not the 3rd index.

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#             0        1       2
friends[1]="Mike" # This modifies the value when the print is ran.
print(friends[1:3])


