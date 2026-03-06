class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def FloorValueData(root,data):
    floor=-1
    while root:
        if root.val==data:
            return root.val
        if root.val<data:
            floor=root.val
            root=root.right
        else: 
            root=root.left
    return floor
root=Node(9)
three=Node(3)
eleven=Node(11)
one=Node(1)
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
data=FloorValueData(root,13)
print(data)