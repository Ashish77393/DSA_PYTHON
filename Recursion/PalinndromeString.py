# 1st method using loop
# def Palindronme(s):
#     newstr=""
#     n=len(s)
#     for i in range(n):
#         newstr+=s[n-(i+1)]
#     if s==newstr:
#         return f'{s} is Palindrome'
#     return f'{s} is  not Palindrome'


# 2nd method using two pointer approach
def Palindronme(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True



def Palindronme(s,l,r):
   
    if l>=r:
        return True
    if s[l]!=s[r]:    
        return False
    return Palindronme(s, l + 1, r - 1)
        
    
    
s="nitis"
l=0
r=len(s)-1
print(Palindronme(s,l,r))
