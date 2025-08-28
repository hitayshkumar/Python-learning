"""
with open("number file.txt","r") as f:
    dat=f.read()
    print(dat)
    ls=[]
    num=''
    j=0
    even=0
    for i in range(len(dat)):
        if(dat[i]==','): # if comma found save num in list
            ls.append(int(num))  # storing the data in list as integer
            if ls[j]%2==0:
                even+=1
            j+=1
            num='' # need to reset num otherwise it will keep adding to old string
        else:
            num+=dat[i] # adding strings wala operation
        
    print(ls)
    print(" Count of even numbers=",even)
"""
#alternate method

with open("number file.txt","r") as f:
    dat=f.read()
    print(dat)
    count = 0
    nums=dat.split(',') # stores in a new list named nums
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)
