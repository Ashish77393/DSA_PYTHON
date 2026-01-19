class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class DlinkedList:
    def __init__(self):
        self.head=None
    def InsertAtStart(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def InsertAtLast(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newnode
            newnode.prev=current
    def InsertAtMiddle(self,val,position):
        newnode=Node(val)
        if position==0:
            self.InsertAtStart(newnode)
            return
        curr=self.head
        count=0
        while curr and count<position-1:
            curr=curr.next
            count+=1
        if curr is None:
            print("positions is out of bounds")
            return 
        newnode.next=curr.next
        newnode.prev=curr
        if curr.next:
            curr.next.prev=newnode
        curr.next=newnode
    def Traverse(self):
        if self.head==None:
            return 0
        current=self.head
        while current is not None:
            print(current.val,end="<->")
            current=current.next
        print("None")
dl=DlinkedList()
dl.InsertAtStart(10)
dl.InsertAtStart(20)
dl.InsertAtStart(30)
dl.InsertAtMiddle(60,9)
dl.InsertAtLast(40)
dl.Traverse()
    
