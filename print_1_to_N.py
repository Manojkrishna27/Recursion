def recursion(i,n):
    if i>n:   # base condition if the satisfy it will stop because return non
        return 
    print(i)   # else it will print i

    recursion(i+1,n)  # use recursion to call back and increment
    
output=recursion(1,5)       # here 1 starts and n stop
