def fib(n):
    if n<=1: # base condition
        return n

    return fib(n-1)+fib(n-2) # fibannoci 

n=4
print(fib(n))  # ans
for i in range(n):
    print(fib(i),end=" ") # fibannoci in sequence manner
