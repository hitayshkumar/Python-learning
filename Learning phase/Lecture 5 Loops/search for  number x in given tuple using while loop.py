t=(1,4,9,16,25,36,49,64,81,100,16,4,76,25,49,2,4,6,9,1)
n=0 #n counts the indices of t also used in loop
num=int(input("enther the number you want to search"))
f=0 # f =1 means found , f=0 means not found
ind=[] #ind is a list that stores the indices of values found in 't' tuple
while n<len(t):
    if (num==t[n]):
        f=1
        ind.append(n) #index number of 't' added/stored in ind[]
    n+=1 
m=0 #counts the index of 'ind'
if(f==1):
    print("Found at: ")
    while(m<len(ind)):
        print(ind[m],"\bth") #prints the index of 't' where the number is found
        m+=1
    print("index(s)")
else:
    print("no such number exists in the following tuple")
print("the tuple is: ",t)