def NextGreaterElement(list):
    # n=len(list)
    # ans=[]
    # for i in range(n):
    #     found=False
    #     for j in range(i+1,n):
    #         if list[j]>list[i]:
    #             ans.append(list[j])
    #             found=True
    #             break
    #     if not found:
    #             ans.append(-1)
    # return ans
    n=len(list)
    ans=[-1]*n
    stack=[]
    for i in range(n):
        while stack and list[i]>list[stack[-1]]:
            idx=stack.pop()
            ans[idx]=list[i]
        stack.append(i)
    return ans
data=[19,4,2,11,6,5,5,5,3,10]
print(NextGreaterElement(data))
