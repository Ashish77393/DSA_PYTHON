def MergeTwoSorted(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    newarr=[]
    for i in range(n1):
        if arr1[i] not in newarr:
            newarr.append(arr1[i])
    for j in range(n2):
        if arr2[j] not in newarr:
            newarr.append(arr2[j])
    return newarr
arr1=[1,2,3,4,5]
arr2=[1,4,5,6,7,8]
print(MergeTwoSorted(arr1,arr2))