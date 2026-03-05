class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def MinimumVal(root):
    if root is None:
        return float('inf')
    left_val=MinimumVal(root.left)
    right_val=MinimumVal(root.right)
    return min(root.val,left_val,right_val)
    
             
            
  
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
data=MinimumVal(root)
print(data)