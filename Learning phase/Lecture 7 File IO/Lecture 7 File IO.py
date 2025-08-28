"""
f = open("E:\Python projects\Learning Phase\Lecture 7 File IO\demo.txt","r") # open a file
data= f.read() # read and return the contents of file
print(data)
print(type(data)) # print the type of content of file
f.close() # always close file after use 

# for anything other than text file
f= open("E:\Python projects\Learning phase\Lecture 7 File IO\demo binary.bin","rb")
data = f.read()
print(data)
f.close()

"""
"""
f= open("E:\Python projects\Learning phase\Lecture 7 File IO\demo.txt","r")
line1 = f.readline() 
print(line1)
line2 = f.readline() # next line will have a empty spae line because all txt files have \n character at end of each line to denote new line which we do not see.
print(line2)
f.close()

"""

# writing to a file
"""
f= open("E:\Python projects\Learning phase\Lecture 7 File IO\demo.txt","a") # append operation
f.write("\nThis is line3")
f.close()
"""
# if file doesn't exist for 'w' or 'a' , python will create it for us
"""
f=open("trial2.txt",'w')
f.write("Hi this is a new file")
f.close()
"""

# combining modes
"""
f=open("trial2.txt","r+")
f.write("abc") # overwrites the file depending on where stream is
f.seek(0) # seek fn used to seeking position in na file
print(f.read()) # reads from after abc because the stream is located after abc now
f.close()
"""

# with syntax
"""
with open("trial2.txt","r") as f:
    data = f.read()
    print(data)
with open("trial2.txt","w") as f:
    f.write(" New data")
"""

# deleting files

"""
import os
os.remove("trial2.txt")
"""
