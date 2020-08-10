# Lesson 22 - 2D Lists and Nested Loops

#All of the elments inside of this number grid can become lists.
#All of the elements in these grids are lists

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid: #for loop
    for col in row:
        print(col)

# results
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0

#print(number_grid[0][0])
# results 1, This is the 0 row and 0 column number


#print(number_grid[2][1])
#results 8

"""
for row in number_grid:
    print(row)

results

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[0]

"""









