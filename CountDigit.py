def CountDigit(n):
    num=n
    count=0
    while(num>0):
        digit=num%10
        count=count+1
        print(digit, end='')
        num=num//10
    
    print("\nlength of digit is =",count)
CountDigit(64537)
