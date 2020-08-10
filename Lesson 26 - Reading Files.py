# Reading Files
# Reading from a text, html files
# A python read command will allow for one to read a file that is stored outside of the python cloud
# r stands for a read only file
# w stands for write where the file can be edited
# a stands for append where information can be appended onto the end of the file. Information can only be added not changed.
# r+ is a reading and writing file

employee_file = open("a", "r") # the open command opens the file
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

#print(employee_file.readable()) # This will return a bullion file that will say if the file is readable.
#print(employee_file.read()) it will read the whole file
#print(employee_file.readline()) # Placing multiple of these will cause the program to read lines one at a time.
#print(employee_file.readline())
#print(employee_file.readlines()) # will read an all the lines and put them inside of an array
#print(employee_file.readlines()[1]) # This will allow for reading specific lines in arrays

#Returns
# Hey this is a test
#
# as;ldkfj
#
#
#
# asd
#
# fa
#
# sdf
#
# asd
#
# f
#
#
# Process finished with exit code 0






