class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def InsertNode(root,newNode):
    while root:
        if root.val>newNode.val:
            root=root.right
        if root.val<newNode.val:
            root=root.left
        
root=Node(5)
three=Node(3)
eight=Node(8)
two=Node(2)
four=Node(4)
root.left=three
root.right=eight
three.left=two
three.right=four
InsertNode(root,Node(6))