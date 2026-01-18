# ist ethod using loopp\
# def Fibbonacci(n):
#     a=0
#     b=1
#     fi=0
#     for i in range(n-1):
#         fi=a+b
#         a=b
#         b=fi
#     return fi



#2nd method using recursion
def  Fibbonacci(n):
    if n==0 or n==1:
        return n
    return Fibbonacci(n-1)+Fibbonacci(n-2)
print(Fibbonacci(7))

        
