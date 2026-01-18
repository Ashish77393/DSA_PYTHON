def Armstrong(number):
    n=number
    arm=0
    while(n>0):
        r=n%10
        arm=r**3+arm
        n=n//10
    if(arm==number):
        return "armstrong number"
    return "Not Armstrong Number"
print(Armstrong(143))
# time complexty(log10(n))
# Space Complexity(O(1))