from collections import deque
class StackusingQueue:
    def __init__(self):
        self.queue=deque()
    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue.popleft()
    def peek(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
s=StackusingQueue()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.pop())
print(s.isEmpty())
print(s.peek())
print(s.size())