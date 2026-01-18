from math import sqrt
def Factor(n):
    arr=[]
    # for i in range(1,n+1):
    #     if n%i==0:           //Brute Force
    #         arr.append(i)
    # return arr
    
    
    # Best Case
    # for i in range(1,n//2+1):
    #     if n%i==0:
    #         arr.append(i)
    # arr.append(n)
    # return arr


    # Optimal Solution 
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            arr.append(i)
            # time complexty=O(Rootn)+O(nlogn)
            #space O(K) k=factors
            if n//i!=i:
                arr.append(n//i)
    arr.sort()
    return arr
print(Factor(60))
