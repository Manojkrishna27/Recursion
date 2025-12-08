# this is the method to find the large and small elements in array with build in function
nums=[1,2,3,4,5]
large=max(nums)
small=min(nums)
print("the largest is",large)
print("the smallest is",small)

# beginner method
arr=[1,3,4,2,5]
large=arr[0]
small=arr[0]
for i in arr:
    if i >large:
        large=i
    if i<small:
        small=i
print("the largest is ",large)
print("the small is ",small)
        

