def DecimalToBinary(n):
    temp=n
    list=[]
    while temp>0:
        n=temp%2
        list.append(n)
        temp=temp//2
    list=list[::-1]
    return list
n=23
def BinaryToDecimal(str):
    decimal=0
    power=len(str)-1
    for i in range(len(str)):
        if str[i]=='1':
            decimal+=2**power
        power-=1
    return decimal
         
data=BinaryToDecimal("10111")
print(DecimalToBinary(data))
print(data)