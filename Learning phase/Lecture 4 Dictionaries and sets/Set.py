"""
collection={1,2,3,4,"hello","world",4}
print(collection,type(collection))  #duplicate values are ignored
print(len(collection)) #duplicate values are ignored in length as well

col={} #this is not an empty set, this is an empty dictionary
print(type(col))
#in order to create an empty set, 
coll=set() #empty set; syntax
print(type(coll))

"""

#set methods
"""
# 1) set.add(el)

collection=set()
collection.add(1)
collection.add(2)
collection.add("college")

collection.add((1,3,2,4))
# collection.add([4,5,3,6]) #error; unhashable type / mutable list data in immutable value of set
print(collection)


# 2) set.remove(el)
collection.remove(2)
print(collection)
#collection.remove(7) #error; 7 doesn't exist


# 3) set.clear() # empties the set
collection.clear()
print(collection)

# 4) set.pop() # removes a random value from the set
coll={3,6,5,7,2,5,9,1}
print("set coll: ",coll)
coll.pop()
coll.pop()
print(coll)

"""
# 5) set.union(set2)
"""
s1={2,3,2,4,8,3,2}
s2={7,8,9,6,8,6,5}
print(s1.union(s2)) #s1 stays same
print(s1)

s3=s1.union(s2)
print(s3)
"""

# 6) set.intersection(set2)

s1={2,3,2,4,8,3,2}
s2={7,8,9,6,8,6,5}

s3=s1.intersection(s2)
print(s3)
