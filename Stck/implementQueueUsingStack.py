class ImplementQueueUsingStack:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def push(self,item):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(item)
        while self.st2:
            self.st1.append(self.st2.pop())
    def pop(self):
        if not self.st1:
            return "stack is empty"
        e=self.st1.pop()
        return e
    def peek(self):
        if not self.st1:
            return "stack is empty"
        return self.st1[-1]
    def size(self):
        return len(self.st1)
s=ImplementQueueUsingStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.pop())
print(s.size())
print(s.peek())