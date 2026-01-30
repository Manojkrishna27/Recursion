# pointer method
arr=[0,2,3,4,0,1,0]
j=0
for i in range(len(arr)):
    if(arr[i]!=0): # if not 0 
        arr[i],arr[j]=arr[j],arr[i] # swap
        j+=1 # slow pointer
print(arr) 