class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def heightTree(node):
    if node is None :
            return 0
    left=heightTree(node.left)
    right=heightTree(node.right)
    return 1+max(left,right)
            
one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)
ten=Node(10)
one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
six.left=eight
eight.right=nine
nine.right=ten
print(heightTree(one))