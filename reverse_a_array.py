'''for reverse a array we can use easy method '''
 
 # using slicing method

arr=[1,2,3,4]
rev=arr[::-1]  # slicing and -1 is reverseing
print(rev)

# method 2 using build in function
arr=[1,2,3,4]
arr.reverse()
print(arr)

# using logic
arr=[2,3,4,5]
reverse=[]
for i in range(len(arr)-1,-1,-1):  # create  this loop carefully here we need to reverse start from len(arr)-1 if len 4 -1 so 3
                                   # then end in -1 because array index start from 0 and in python it will not excute end range value so we use -1
                                   # and for decrement we use -1
    reverse.append(arr[i])         # here we appending the arr[i] from reverse order it will append in empty array
print(reverse)