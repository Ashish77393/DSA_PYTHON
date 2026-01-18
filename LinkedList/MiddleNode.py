class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def MiddleElement(head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

        return slow 