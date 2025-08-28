print("Hi, Please enter name three of your favourite movies:")
"""
m1=input("1st_ ")
m2=input("2nd_ ")
m3=input("3rd_ ")
fav_mov=[m1,m2,m3]
print("fav movies are: ",fav_mov)
"""
#alternate method using append nethod
"""
fav_mov=[]
m1=input("1st_ ")
m2=input("2nd_ ")
m3=input("3rd_ ")
fav_mov.append(m1)
fav_mov.append(m2)
fav_mov.append(m3)
print("Your fav movies are: ",fav_mov)
"""
#another alternate using append method

mov=[]
mov.append(input("1st: "))
mov.append(input("2nd: "))
mov.append(input("3rd: "))
print("your fav movies are: ",mov)
print("number of movies you like are :",len(mov))