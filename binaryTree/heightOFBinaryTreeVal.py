class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def BinaryTreeHeight(root,val):
        temp=root
        while temp is not None:
            if temp.val==val:
                 return temp
            elif val<temp.val:
                temp=temp.left
            else:
                temp=temp.right
        return None
root=Node(9)
three=Node(3)
eleven=Node(11)
two=Node(2)
seven=Node(7)
ten=Node(10)
fiveten=Node(15)
four=Node(4)
eight=Node(8)
fourteen=Node(14)
root.left=three
root.right=eleven
three.left=two
three.right=seven
eleven.left=ten
eleven.right=fiveten
seven.left=four
seven.right=eight
fiveten.left=fourteen
data=BinaryTreeHeight(root,10)
if data:
     print("data found in binary search tree",data.val)
else:
     print("data not found ",None)