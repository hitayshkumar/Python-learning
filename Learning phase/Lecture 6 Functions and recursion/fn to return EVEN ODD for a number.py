def odd_even(a):
    if a%2==0:
        return "Number is EVEN"
    else:
        return "Number is ODD"

n=int(input("Please enter the number to check if it is even of odd: "))
print(odd_even(n))