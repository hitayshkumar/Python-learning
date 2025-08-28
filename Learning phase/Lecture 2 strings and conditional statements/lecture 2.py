"""
str1 = "this is a string."
str2 = 'this is another string'
str3= '''this is yet another string'''
str4 = "this is hitesh's string"
print("This is line 1\nThis is line 2\t this is line after tab")

# concatenation of srings
str5 = str1+str2
print(str5)
str6 = str5+" addition"
print(str6)
length6=len(str6)
print("length og string 6 =",length6," characters")

#indexing

print(str5,"\n11th position character","'",str5[11],"'")
"""
"""
#slicing of strings
str= "ApnaCollege"
print(str[1:])
print(str[1:5])
print(str[:len(str)]) #unnecessary bc same as pirint(str)
#assigning via slicing
newstr=str[5:9]
print(newstr)
"""
"""
#negative index
str ="Apple"
print(str[-3:-1])  # starting from last character, it gets -1 and then others negative sequencially
"""

"""
# string functions
str='i am a coder.'
print("Original string: ",str)
print("endswith 'er': ",str.endswith("er.")) # returns true if string ends with substr.
print("endswith 'app':",str.endswith("app"))
str=str.capitalize()
print(" 1'st letter Capitalaized : ",str)
print("replacing substrings: ",str.replace("coder","plant")) #can also replace subsrtrings

print(str.find("coder")) #gives index of first character of the word to find
print(str.find("tree")) #gives -1 because tree doesn't exist in the string
print(str.count("a")) #gives number of occurences of substr in the main string
"""

#conditional statements
"""
age =int(input("Enter age of the candidate: "))
if(age>=18):
    print("eligible for licence")
else:
    print("ineligible for license")

"""    
"""
light= "red"
if(light=="green"):
    print("Go") #tab space = indentation  in replacement to {} in c++
elif(light=="Yellow"):
    print("Ready")
elif(light=="red"):
    print("Stop")

print("the code has ended")
"""

#nesting in conditional statements

age=int(input("Enter the age of the candidate"))
if(age>=18):
    if(age>=80):
        print("Too old to drive")
    else:
        print("Eligible for driving license")
else:
    print("Too young for driving license")