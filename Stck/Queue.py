class Queue:
    def __init__(self):
        self.list=[]
    def isEmpty(self):
        return len(self.list)==0
    def enQueue(self,item):
        self.list.append(item)
    def Dequeue(self):
        if len(self.list)==0:
            return "Queue is empty"
        e=self.list.pop()
        return e
    def Front(self):
        if len(self.list)==0:
            return "Queue is empty"
        return self.list[0]
    def Rare(self):
        if len(self.list)==0:
            return "Queue is empty"
        return self.list[-1]
    def Size(self):
        return len(self.list)
Q=Queue()
Q.enQueue(10)
Q.enQueue(20)
Q.enQueue(30)
Q.enQueue(40)

for item in Q.list:
    print(item ,end=" <-")
print("")
print("Dequeue element is",Q.Dequeue())
print("Front items is : ",Q.Front())
print("Rare items is : ",Q.Rare())

