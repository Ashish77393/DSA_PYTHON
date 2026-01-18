def SumNaturalNumber(n):
    if n==0:
        return 0                 #functional recursion
    return n+SumNaturalNumber(n-1)
print(SumNaturalNumber(0))