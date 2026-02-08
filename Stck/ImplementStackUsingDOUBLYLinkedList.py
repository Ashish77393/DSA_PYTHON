class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def Push(self,value):
        newnode=Node(value)
        newnode.next=self.top
        if self.top is not None:
            self.top.prev=newnode
        self.top=newnode
        print(f'{value} is pushed')
    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        temp=self.top
        print(f'{temp.data} is poped from list')
        self.top=self.top.next
        if self.top is not None:
            self.top.prev=None
    def peek(self):
        if self.top is None:
            return "stack is empty"
        return self.top.data
    def Display(self):
        if self.top is None:
            return "Stack is Empty"
        temp = self.top
        print("Stack elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
s=Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
print(s.peek())
s.pop()
s.Display()
