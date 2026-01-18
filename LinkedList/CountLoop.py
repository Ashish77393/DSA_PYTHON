class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    # def CountsLoop(self,head):
    #     mydict={}
    #     count=0
    #     temp=head
    #     while temp is not None:
    #         if temp not in mydict:
    #             mydict[temp]=count
    #             count+=1
    #             temp=temp.next
    #         else:
    #             return count-mydict[temp]
    #     return 0


    #optimal Solutions
    def CountsLoop(self,head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                count=1
                while slow!=fast:
                    slow=slow.next
                    count+=1
                return count 
        return 0
# Create nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b   

print(a.CountsLoop(a))  
