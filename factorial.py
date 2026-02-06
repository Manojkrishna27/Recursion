def factorial(n):
    if n==0 or n==1: # in factorial 0 and 1 is 1 
        return 1
    return n*factorial(n-1)  # here we use recursion for finding factorial

output=print(factorial(4))

fact=1
n=4
for i in range(1,n+1):
    fact*=i
print(fact)