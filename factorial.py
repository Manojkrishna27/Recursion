def factorial(n):
    if n==0 or n==1: # in factorial 0 and 1 is 1 
        return 1
    return n*factorial(n-1)  # here we use recursion for finding factorial

output=print(factorial(4))