from collections import deque
from multiprocessing import current_process
# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Iterative function for inorder tree traversal
def inorderIterative(root):
 # start writing from here
 # create empty stack
  stack = deque()
 # create variable to store current node
  currentNode = root
 # loop until stack is empty or current is not none
  while stack or currentNode:
 # keep pushign into stack until current -> left exist
    if currentNode:
 # push the current node and move current to left child
      stack.append(currentNode)
      currentNode = currentNode.left
 # pop from stack and make current = poped node
    else:
 # print the current node
      currentNode = stack.pop()
      print(currentNode.data, end = ' ')
 # make current = current -> right
      currentNode = currentNode.right
# Iterative function for preorder tree traversal
#def preorderIterative(root):
 # start writing from here


# Iterative function for postorder tree traversal
#def postorderIterative(root):
 # start writing from here
 

# Iterative function for levelorder tree traversal
def levelorderIterative(root):
 # start writing from here

 # base case : check whether root exists
 if not root:
     return
 # create an empty queue
 queue = deque()

 # push the root into queue
 queue.append(root)
 #loop until queue empty
 while queue:
 #pop
     currentNode = queue.popleft()
     print(currentNode.data, end = ' ')
 #push left
     if currentNode.left:
          queue.append(currentNode.left)
 #push right
     if currentNode.right:
          queue.append(currentNode.right)
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    inorderIterative(root)
    levelorderIterative(root)