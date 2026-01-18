def matrix3Sum(arr):
    # Better Solutions
    result=set()
    for i in range(len(arr)):
        myset=set()
        for j in range(i+1,len(arr)):
            third=-(arr[i]+arr[j])
            if third in myset:
                temp=[arr[i],arr[j],third]
                temp.sort()
                result.add(tuple(temp))
            myset.add(arr[j])
    return [list(ans) for ans in result]
arr=[-1,0,1,2,-1,4]
print(matrix3Sum(arr))
