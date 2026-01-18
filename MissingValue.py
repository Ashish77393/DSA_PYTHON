def MissingValue(arr):
    # n=len(arr)
    # for i in range(n):
    #     if arr[i]!=i:
    #         return i
    # return n



    #second method
    # n=len(arr)
    # freq_map={}
    # for i in range(n+1):
    #     freq_map[i]=0
    # for num in arr:
    #     freq_map[num]=1
    # for k,v in freq_map.items():
    #     if v==0:
    #         return k


    #Third method 
    n=len(arr)
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    sum1=n*(n+1)/2
    mising=sum1-sum
    return int(mising)
arr=[0,1,2]
print(MissingValue(arr))
