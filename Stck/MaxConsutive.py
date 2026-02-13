def MaxConsutive(list,k):
    n=len(list)
    max_len=0
    for i in range(n):
        count=0
        val=k
        for j in range(i,n):
            if list[j]==1:
                count+=1
            elif list[j]==0 and val>0:
                val-=1
                count+=1
            else:
                break
            max_len=max(count,max_len)
    return max_len
list=[1,1,1,0,1,1,0,0,0,1,1,0,0,1]
print(MaxConsutive(list,2))
            
        

            

