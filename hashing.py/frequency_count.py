def countfreq(n):
    freq={}
    for i in n:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    result=[]
    for key ,value in freq.items():
        result.append([key,value])
    return result
n=[1,2,1,2,3]
print(countfreq(n))