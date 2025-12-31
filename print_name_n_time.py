'''Recursion is a programming technique where a function calls itself directly or
 indirectly to solve a problem, by breaking it down into smaller subproblems 
 until it reaches a base case that stops further calls.

'''
def recursion(i,n):  # create a function 
    if i>n:     # base condition 
        return  
    print("manoj")
    recursion(i+1,n) # call itself until it satisfy the condition 

output=recursion(1,6)