def Factorial(n):
    if n==0 or n==1:
        return 1
    return n*Factorial(n-1)
n=int(input("enter a number : "))
fact=Factorial(n)
print(fact)



# Using Loop are not possible for large numbers
# def Factorial(n):
#    fact=1
#    if n==0 or n==1:
#         return fact             
#    for i in range(n):
#       fact=fact*i
#    return fact
# n=int(input("enter a number : "))
# fact=Factorial(n)
# print(fact)