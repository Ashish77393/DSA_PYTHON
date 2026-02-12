def ColllisionStack(list):
    stack=[]
    for data in list:
        while stack and stack[-1]>0 and data<0:
            if stack[-1]<-data:
                stack.pop()
                continue
            elif stack[-1]==-data:
                stack.pop()
            break
        else:
            stack.append(data)
    return stack
                          

           
list=[4,7,1,2,-3,-7,17,15,-18,-19]
print(ColllisionStack(list))