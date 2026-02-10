class Stack:
    def __init__(self):
        self.stack=[]
    def Postfix(self,infix):
        precedence = {
               '+': 1,
               '-': 1,
               '*': 2,
               '/': 2,
               '^': 3,
               '(': 0,
               ')': 0
                     }
        ans=''
        for ch in infix:
            if ch.isalnum():
                ans+=ch
            elif ch=='(':
                self.stack.append(ch)
            elif ch==')':
                while self.stack and self.stack[-1]!='(':
                    ans+=self.stack.pop()
                self.stack.pop()
            else:
                while(self.stack and precedence[self.stack[-1]]>=precedence[ch]):
                    ans+=self.stack.pop()
                self.stack.append(ch)
        while self.stack:
                ans+=self.stack.pop()
        return ans

                
s = Stack()
print(s.Postfix("A+B*(C-D)*A^E"))