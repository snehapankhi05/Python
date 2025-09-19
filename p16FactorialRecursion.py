def factorial(n):
    if(n<2):
        return 1
    else:
        return n*(factorial(n-1))

n=int(input("Please enter number"))
fac=factorial(n)
print(fac)