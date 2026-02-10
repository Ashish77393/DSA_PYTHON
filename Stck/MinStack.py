class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def getMin(self):
        if len(self.stack)==0:
            return "Stack is empty"
        return min(self.stack)
        
    def pop(self):
        if len(self.stack)==0:
            return "stack is Empty"
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]
    def display(self):
        if len(self.stack)==0:
            return "Stack is Empty"
        else:
            for data in reversed(self.stack):
               print(data,end=' ')
s=MinStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print("Min element is : ",s.getMin())
print("Popped element is :",s.pop())
print("peek elemnet is : ",s.peek())
s.display()

