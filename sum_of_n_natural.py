# method 1 using recursion
def natural(n):
    if n==0:
        return
    else:
        return (n*(n+1)//2)
    
output=print(natural(2))

# method 2 using  for loop
n=2
s=0
for i in range(1,n+1):
    s+=i
print(s)