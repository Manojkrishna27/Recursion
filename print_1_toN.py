def recursion(i,n): 
    if i>n: # base condition if the satisfy it will stop because return non
        return
    
    print(i)   # else it will print i
    recursion(i+1,n) # use recursion to call back and increment

n=int(input())       # i use n as a input 
output=recursion(1,n)  # here 1 starts and n stop


