class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
one=Node(1)
two=Node(2)
Three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)
ten=Node(10)
five.left=Three
five.right=four
Three.left=two
Three.right=nine
four.left=eight
four.right=ten
eight.left=one
eight.right=six
# def preorder(node):
#     if node==None:
#         return
#     print(node.val,end=" ")
#     preorder(node.left)
#     preorder(node.right)
# preorder(five)

# def Inorder(node):
#     if node==None:
#         return
    
#     Inorder(node.left)
#     print(node.val,end=" ")
#     Inorder(node.right)
# Inorder(five)


def PostOrder(node):
    if node==None:
        return
    
    PostOrder(node.left)
    PostOrder(node.right)
    print(node.val,end=" ")
PostOrder(five)