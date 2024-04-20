# 2 modes for writing in the file
# "a", "w"

'''f=open("D:\PYTHON PRACTICE/demofile.txt","a")
f.write("Now this file has one more content")
f.close()

# open and read the file after the appending
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.read())'''

# 1st open the file overwrote the content.
f=open("D:\PYTHON PRACTICE/demofile.txt","w")
f.write("Yes, finally now we have overwrittten the content")
f.close()

# open and read the file after the appending
f=open("D:\PYTHON PRACTICE/demofile.txt","r")
print(f.read())

# creating a new file
# "x" - create a file
# "a" - append file
# "w" - will write or createa a file



f=open("myfile.txt","w")
f.write("HI , pavan how are brother")

f=open("myfile.txt","r")
print(f.read())
f.close()

# how to delete a file 
import os
os.remove("myfile.txt")

# check if the file exist and give the condition
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("thi given file is not exists")

# how to delete the existing folder
# import os
# os.rmdir(".idea") # this command can only  remove empty folder

