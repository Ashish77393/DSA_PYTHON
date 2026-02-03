def SubsetSum(index,total,nums,result):
    if index>=len(nums):
        result.append(total)
        return
    sum=total+nums[index]
    SubsetSum(index+1,sum,nums,result)
    sum=total
    SubsetSum(index+1,sum,nums,result)
index=0
sum=0
nums=[5,9,3]
result=[]
SubsetSum(index,sum,nums,result)
print(result)