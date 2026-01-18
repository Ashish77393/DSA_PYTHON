# def SecondLargest(arr):
#     n=len(arr)
#     largest=float('-inf')
#     slargest=float('-inf')
#     for i in range(0,n):
#         largest=max(largest,arr[i])
#     for i in range(0,n):
#         if arr[i]<largest and slargest<arr[i]:
#             slargest=arr[i]
#     return slargest



def SecondLargest(arr):
    n=len(arr)
    largest=float('-inf')
    slargest=float('inf')
    for i in range(0,n):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
        elif arr[i] < largest and arr[i] > slargest:
            slargest = arr[i]
    return slargest
        

arr=[4,6,3,6,6,3]
print(SecondLargest(arr))