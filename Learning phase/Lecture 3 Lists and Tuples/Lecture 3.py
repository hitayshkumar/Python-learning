# Lists are similar to arrays in c++

#for example
"""
marks=[90,65,45,34,75,23]
print(marks)
print(type(marks))
print(marks[3],marks[5])
print(len(marks))
"""
#it can store different types ofdata together as well
"""
Student=["Karan",24,"Delhi"]
print(Student)
"""

#Lists are mutable in python while strings are not
"""
Student=["Karan",24,"Delhi"]
Student[0]="Hitesh"
print(Student)
"""

# slicing in lists
"""
marks=[90,65,45,34,75,23]
print(marks[2:5]) #ending index is not included in the result
#negative slicing also possible
print(marks[-4:-1])
print(marks[1:]) 
"""
# list methods
"""
marks.append(89)
print(marks)

marks.sort() #sorting at ascending order
print(marks)

marks.sort(reverse=True) #sorting at descendding order
print(marks)

marks.reverse()#reversing the list
print(marks)

marks.insert(3,67) #inserts in between adding to length of list
print(marks)

"""

#also does alphbetical sorting
"""
fruit=["mango","apple","banana","kiwi","apricot","orange"]
fruit.sort()
print(fruit)
"""
# remove entries
"""
marks=[90,65,45,34,75,23]
print("Initially: ",marks)
marks.remove(45)  #remove takes element as value
print("After removal of 45: ",marks)
marks.pop(3) #pop takes index as value
print("Marks after deleting entry at idx 3:",marks)
"""

#tuples
"""
tup=(2,1,3,1)
print(type(tup))
print(tup[1:3])
"""

#tuple methods
tup=(2,1,3,1)
print(tup.index(1))
print(tup.count(1))
