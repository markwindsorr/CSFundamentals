"""
A Python Binary Tree Implementation

"""

class Node: 

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def print_in_order(node):

		if node:

			# Recursion on left child
			print_in_order(node.left)

			# "Visit" and access the current nodes data
			print(node.data)

			# Recursion on right child
			print_in_order(node.right)

	def print_pre_order(node):

		if node: 

			# "Visit" and access the current nodes data
			print(node.data)

			# Recursion on left child
			print_pre_order(node.left)

			# Recursion on right child
			print_pre_order(node.right)

	def print_post_order(node)

		if node:

			# Recursion on left child
			print_post_order(node.left)

			# Recursion on right child
			print_post_order(node.right)

			# "Visit" and access the current nodes data
			print(node.data)