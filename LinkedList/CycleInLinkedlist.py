class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    # def CycleLinkedList(self,head):
    #     temp=head
    #     myset=set()
    #     while temp is not None:
    #         if temp  in myset:
    #             return True
    #         else:
    #             myset.add(temp)
    #             temp=temp.next
    #     return False
    
    def CycleLinkedList(self,head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

        