t=('c','d','a','a','b','b','a')
print("initial tuple: ",t)
n=t.count('a')
print("number of 'A' grade students are: ", n)
#now store this data from this tuple in a new List
T=[]
n=0
while n<len(t):
    T.append(t[n])
    n+=1
print("New List data:",T)