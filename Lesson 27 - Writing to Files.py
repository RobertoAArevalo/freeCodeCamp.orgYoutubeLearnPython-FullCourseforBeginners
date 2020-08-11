#Lesson 27 - Writing to Files

#writing and appending files to python

a_file = open ("index.html", "w") #r is to read a file, a is to append or add to the file, w is to write or complete replace the file.
                          # Inserting a new title for a file allows for creating a new file. a1 for example.
a_file.write("<p> This is HTML </p>") # \n adds a new line

a_file.close()

#a_file.write("Toby - Human Resources") # This is how one adds to another existing file. If the code is ran twice than it will repeat the action again.

# Overwrite an existing file, write a new file, or append to the end of a file

