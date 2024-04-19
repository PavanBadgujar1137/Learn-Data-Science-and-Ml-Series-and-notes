# file handling - open()
f=open("demofile.txt")
# or
f= open("demofile.txt","rt")

# there are 4 different modes of opening files
# "r", "a", "w", "x"

# to open the file using built in open() and read()
f= open("demofile.txt","r")
print(f.read())

# open a file in different location
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.read())

# read only the part of the file
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.read(7))

#  how to read lines
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.readline())
print(f.readline())

# lloping through the line by line
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
for i in f:
    print(i)

# How to close the open file
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.readline())
f.close()
    