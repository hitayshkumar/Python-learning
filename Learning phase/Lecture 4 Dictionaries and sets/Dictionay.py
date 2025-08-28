#creating a dictionary
# format "key":"value" 
"""
info={
    "name":"hitesh",   # a comma is important after each statement
    "subjects":["python","c","java","c++"],
    "topics":("dict","set"),
    "age": 31,
    "is_adult":True,
    "marks":94.4,
}


info["name"]="ranjna" #assigning new value to an existing key
info["surname"]="saklani" # adding new key:value pair is simple
print(info)
"""

#creating a null dict is also possible
"""
dic={}  #empty/null dictionary
print(dic)
"""""

#nested dictionary

stu={
    "name":"rahul kumar",
    "sub": {
        "phy":97,
        "chem":98,
        "math":89,
    }
}
print(stu)
print("His marks in chemistry: ",stu["sub"]["chem"])


#dictioinary methods

# 1) dict.keys() returns all the keys in a dict
"""print(list(stu.keys()))   #typecasting in the form of a list
#or
lst=(list(stu.keys()))
print(lst)
print(len(stu))  #ffinding the length of a dictionary
"""


# 2) dict.values() returns all the values in a dict
"""
print(stu.values())
lst=list(stu.values())  #here we typecasted the values of the dict and essentially stored a dict which was as a value in the outerinto a list
print(lst)
"""


# 3) dict.itms() returns all key:val pairs as tuples
"""
print(stu.items())
lst=list(stu.items())
print(lst)
print(lst[1])
"""


# 4) dict.get("key") #returns the value acc to key
"""
print(stu.get("name")) # is similar to,
print(stu["name"])
#but for non existent keys,
#  print(stu["name1"])   # gives error
print(stu.get("name1"))  #retrns 'None' without error
"""

#5)dict.update(newdict)

stu.update({"city":"delhi"})
print(stu)
#alternate mthod
newdict={
    "gender":"male",
}
stu.update(newdict)
print(stu)