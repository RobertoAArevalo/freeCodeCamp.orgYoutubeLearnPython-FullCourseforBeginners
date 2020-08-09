#Lesson 20 - For Loops

# It can Loop through a series of strings.
#for will be used  in every iteration on the for loop and each time it will have a different value (most likely)

"""
friends = ["Jim", "Karen", "Kevin"]

for letter in "Giraffe Academy":
    print(letter)

results

G
i
r
a
f
f
e
 
A
c
a
d
e
m
y

Process finished with exit code 0
"""

"""
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

Jim
Karen
Kevin
"""


"""
friends = ["Jim", "Karen", "Kevin"]
for index in range(10):
    print(index)

results 

0
1
2
3
4
5
6
7
8
9

"""


"""
friends = ["Jim", "Karen", "Kevin"]
for index in range(3, 10):
    print(index)

results
3
4
5
6
7
8
9
"""



"""
friends = ["Jim", "Karen", "Kevin"]
#len(friends) will return 3
for index in range(len(friends)):
    print(friends[index])
    # Each time it is passed throught friends[0,1,2]

results

Jim
Karen
Kevin

"""

friends = ["Jim", "Karen", "Kevin"]
for index in range(5):
    if index == 0:
        print("first Iteration") # it will print one thing on first iteration
    else:
        print ("Not first") # and something different on 2nd time.

"""
results
first Iteration
Not first
Not first
Not first
Not first

"""