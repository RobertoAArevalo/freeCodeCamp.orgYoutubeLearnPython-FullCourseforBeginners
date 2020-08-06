#Lesson 10 - List Functions

#There are many different functions that can be used to modify lists and get information about the lists.
# An .extend() function will allow to pass a list into a list or add a list after a list.
# friends.append("Creed") can add another name to the end of the list
# friends.insert(1, "Kelly")
    #This insert function will add a name to the specific part of a list.

#friends.remove("Jim") can remove a specific name from a list
#friends.clear() Will remove all names or values from the list.
#friends.pop() Will remove the last element off of the list.
# print(friends.index("Kevin")) will retrieve the index location of the given name.
#print(friends.count("Jim")) Will tell me how many values of Jim there are in the list.

#friends.sort() Will print the list in alphabetical order.
#random_numbers.sort() Will place numbers in ascending order.
#random_numbers.reverse() will reverse the numbers in the list.



random_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar","Toby"]

friends2 = friends.copy() # This will copy the list
print(friends2)

#These are some basic list functions..
