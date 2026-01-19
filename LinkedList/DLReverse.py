class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class DlLinked:
    def __init__(self):
        self.head=None
    def Reverse(self,head):
        if self.head is None :
            return head
        else:
            curr=head
            prev=None
            while self.head is not None:
                front=curr.next
                curr.next=prev
                curr.prev=front
                prev=curr
                curr=front
            return head
