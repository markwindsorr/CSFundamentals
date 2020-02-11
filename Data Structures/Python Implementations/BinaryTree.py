"""
A Python Binary Tree Implementation

"""

class Node: 

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	# Create root
	root = Node(1)
	''' The current Tree
     
        1 
      /   \
     None  None

     '''

     # Add Left and Right Nodes to the root

     root.left = Node(2)
     root.right = Node(3)

     ''' 2 and 3 become left and right children of 1 
             1 
          /     \
        2        3 
      /   \     /  \
    None None  None None
   '''

   	 root.left.left = Node(4)
   	 '''4 becomes left child of 2 
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None'''