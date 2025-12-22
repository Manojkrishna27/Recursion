def binarysearch(arr,target):
    high=len(arr)-1
    low=0
    while low <=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7]
target=4
print(binarysearch(arr,target))