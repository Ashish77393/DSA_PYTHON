class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def CeilValueData(root,data):
    ceil=-1
    while root:
        if root.val==data:
            return root.val
        if root.val<data:
            root=root.right
        else: 
            ceil=root.val
            root=root.left
    return ceil
root=Node(9)
three=Node(3)
eleven=Node(11)
one=Node(1)
seven=Node(7)
ten=Node(10)
fiveten=Node(15)
four=Node(4)
eight=Node(8)
fourteen=Node(14)
root.left=three
root.right=eleven
three.left=one
three.right=seven
eleven.left=ten
eleven.right=fiveten
seven.left=four
seven.right=eight
fiveten.left=fourteen
data=CeilValueData(root,66)
print(data)