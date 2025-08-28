lst =[2,1,3,4,5,7,8,4,3,2]

def prnt(lst, idx=0):
    if(idx==len(lst)):
       return
    print(lst[idx])
    prnt(lst,idx+1)

prnt(lst)