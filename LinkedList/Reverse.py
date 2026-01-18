class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    # def ReverseLinked(self,head):
    #     stack=[]
    #     temp=head
    #     while temp is not None:
    #         stack.append(temp.val)
    #         temp=temp.next
    #     temp=head
    #     while temp is not None:
    #         e=stack.pop()
    #         temp.val=e
    #         temp=temp.next
    #     return head

    #optimal_Solutions
    def ReverseLinked(self,head):
        prev=None
        curr=head
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev


head=Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.ReverseLinked(head)