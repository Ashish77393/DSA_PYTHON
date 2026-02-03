def CombinationThreeSum(index,total,target,result,subset,k):
    if total==target and len(subset)==k:
        result.append(subset.copy())
        return
    if total > target or len(subset) > k:
        return
    for i in range(index,1000):
     sum=total+i
     subset.append(i)
     CombinationThreeSum(i+1,sum,target,result,subset,k)
     subset.pop()
result=[]
subset=[]
target=9
k=3
CombinationThreeSum(1,0,target,result,subset,k)
print(result)
