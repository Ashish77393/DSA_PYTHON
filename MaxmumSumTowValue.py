def MaximumSum(arr,target):
    # n=len(arr)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if arr[i]+arr[j]==target:
    #             return i,j


    # Optimal Solution
    n=len(arr)
    hash_map={}
    for i in range(n):
        remaining=target-arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[arr[i]]=i
arr=[3,4,5,23,5,3,2,26,7]
target=7
print(MaximumSum(arr,target))
