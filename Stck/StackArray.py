class Stack:
    def __init__(self):
       self.items=[]
    def isEmpty(self):
       return len(self.items)==0
    def push(self,item):
       self.items.append(item)
    def pop(self):
       if len(self.items)==0:
          return "list is empty"
       e=self.items.pop()
       return e
    def top(self):
       if len(self.items)==0:
          return "Stack is empty"
       return self.items[-1]
    def size(self):
       if len(self.items)==0:
          return "Stack is Empty"
       return len(self.items)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Topmost Element is :",s.top())
print("Popped element is :",s.pop())
print("Topmost element is :",s.top())
print('length of stack is : ',s.size())