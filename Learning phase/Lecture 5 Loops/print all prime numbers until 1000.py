n=2 #starting number
total_prime_numbers=0
while n<=100000:
    pr=1  #assuming the number is prime
    ct=2 #counter to divide from 2 until the number being checked
    while ct<n: # initial number 2 isn't chechked because 2!<2
        if(n%ct==0):
            pr=0
            break
        ct+=1
    if(pr==1):
        print(n,end=" ")
        total_prime_numbers+=1

    n+=1
print("\nTotal Prime numbers are :",total_prime_numbers)