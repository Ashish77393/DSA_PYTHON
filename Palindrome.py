def Palindrome(number):
    n=number
    rev=0
    while(n>0):
      newnumber=n%10
      rev=rev*10+newnumber
      n=n//10
    if(number==rev):
       return True
    return False
print(Palindrome(123214))




