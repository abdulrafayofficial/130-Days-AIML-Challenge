# File Handling
'''
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''

f = open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt")
# print(f.read())


#Using the with statement:
with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt") as f:
    print(f.read())
# Then you do not have to worry about closing your files, the with statement takes care of that.



#you must close the file if you're not using the close() statement.

f = open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt")
print(f.readline())
f.close()#Always a good practice to close the file...


f = open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt")
# You can return one line by using the readline() method:
print(f.readline())
f.close()


#By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Example
# Return the 5 first characters of the file:

with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt") as f:
  print(f.read(5))




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Write to an Existing File

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content




with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt","a") as f:
   f.write("Now the file has more Content!...")

#open and read the file after appending:
with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt") as f:
   print(f.read())
   

# Overwrite Existing Content

with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt","w") as f:
   f.write("Whoops! I have deleted the Content....")

with open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\text.txt") as f:
   print(f.read())
   
# Deleting a File:
# To delete a file, you must import the OS module, and run its os.remove() function:

import os
if os.path.exists('Day11_File IO — open, read,write, append, with statement, CSV basics\\myfile.txt'):
   os.remove(r"Day11_File IO — open, read,write, append, with statement, CSV basics\\myfile.txt")
else:
   print("The file does not exist")
   

#    Create a New File

o = open(r"Day11_File IO — open, read,write, append, with statement, CSV basics\\myfile.txt","x")
o.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Reading and Writing CSV Files in Python

# However, we first need to import the module using:
import csv
path = 'Day11_File IO — open, read,write, append, with statement, CSV basics\\test.csv'

# with open(path,'r') as f:
#    f = csv.reader(f)
#    for line in f:
#       print(line)

# — — — — — — — — — — — — Writing a CSV — — — — — — — — — —

data = [
   ['EMPID', 'FNAME', 'LNAME', 'HIREDT', 'JOBID', 'SAL'],
   [1, 'Blaine', 'Calhoun', '1998-03-02', 55, 8400],
   [2, 'Mark', 'Farley', '1996-08-03', 55, 8100]
   [3, 'Rafay', 'Rafay', '1996-08-03', 55, 1200]
]

with open('employees-out-1.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerows(data)

