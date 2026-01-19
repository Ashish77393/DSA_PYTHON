class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    def oddEvenPrint(self,head):
        mylist=[]
        temp=head
        if temp is None or temp.next is None:
            return head
        while temp and temp.next:
            mylist.append(temp.val)
            temp=temp.next.next
        temp=head.next
        while temp is not None:
            mylist.append(temp.val)
            temp=temp.next.next
        temp=head
        index=0
        while temp is not None:
            temp.val=mylist[index]
            index+=1
            temp=temp.next
        return head