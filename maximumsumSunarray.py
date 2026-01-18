def maximumSumsubarray(arr):
    # max_sum=0
    # n=len(arr)
    # for i in range(n-1):
    #     sum=0
    #     for j in range(i,n):
    #         sum+=arr[j]
    #         max_sum=max(max_sum,sum)
    # return max_sum



    # Optimal Solution
    max_sum=float('-inf')
    curr_sum=0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        if curr_sum>max_sum:
         max_sum=curr_sum
        if curr_sum<0:
         curr_sum=0
    return max_sum
    

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maximumSumsubarray(arr))