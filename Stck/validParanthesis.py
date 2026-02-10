def ValidParanthesis(str):
    stack=[]
    for i in range(len(str)):
        if str[i]=='(' or str[i]=='{' or str[i]=='[':
            stack.append(str[i])
        else:
            if len(stack)==0:
                return False
            ch=stack.pop()
            if(
             (str[i]==')' and ch=='(') or (str[i]=='}' and ch=='{') and (str[i]==']' and ch=='[')
            ):
                continue
            else:
                return False
    return len(stack)==0 
str="((()))["
print(ValidParanthesis(str))