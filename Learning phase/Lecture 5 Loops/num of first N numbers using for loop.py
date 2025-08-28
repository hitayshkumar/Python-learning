n=int(input(" Enter upto which you need to find the sum: "))
sum=0
for i in range(1,n+1): # default step is 1 already
    sum+=i
print("sum=",sum)
