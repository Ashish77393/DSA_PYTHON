class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinglyLinked:
    def __init__(self):
        self.head=None
    def Append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def Traverse(self):
        if self.head is None:
            print ("is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()
    def AppendPosition(self,val,position):
        newnode=Node(val)
        if position==0:
            newnode.next=self.head
            self.head=newnode
            return 
        else:
            curr=self.head
            prev=None
            count=0
            while curr is not None and count<position:
                prev=curr
                curr=curr.next
                count+=1
              
            prev.next=newnode
            newnode.next=curr

        

d=SinglyLinked()
d.Append(10)
d.Append(20)
d.AppendPosition(40,6)
d.Append(30)
d.Traverse()
        