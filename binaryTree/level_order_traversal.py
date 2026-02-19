# level order Travelsal
# print data using 1-2-3-4-5-6
# print data using loop  beacause data printed line by line
from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def levelOrderTraversal(node):
    result=[]
    queue=deque({})
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result
one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven

print(levelOrderTraversal(one))


