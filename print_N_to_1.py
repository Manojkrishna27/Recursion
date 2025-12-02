def recursion(n,i):
    if n>=i: # here compareing n >= because it will end in 1 we want 1 so =
        print(n) 
    else:
        return
    recursion(n-1,i) # for n to 1 we use n-1

output=recursion(10,1)