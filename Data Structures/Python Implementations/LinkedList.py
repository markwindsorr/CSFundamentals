"""
Python Linked List Implementation

** FIX THIS

"""

class Node:

	# Constructor for a linked list node
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Contruction to initialize the head
	def __init__(self):
		self.head = None

	# Print List
	def print_list(self):
		if head == None:
			print("Your list is empty")
			return 

		current_node = self.head
		while current_node != None:
			print(current_node.value)
			current_node = current_node.next


	
	# Append new node at the end of linked list
	# If head is empty, set the new node to head
	# Otherwise traverse to the end of the list and 
	# set the last nodes next node to the new node
	def append(self, new_data):
		
		if self.head == None:
			self.head = Node(new_data)
			return

		current_node = self.head
		while current_node:
			current_node = current_node.next

		current_node.next = Node(new_data)

	# Inserting a new node at the beginning
	def push(self, new_data):

		if self.head == None:
			self.head = Node(new_data)
			return

		previous_head = self.head
		self.head = Node(new_data)
		self.head.next = previous_head

	# Reverse Linked List
	def reverse_list(self):

		new_head = None
		current_node = self.head
		while current_node:
			new_head.push(current_node.data)
			current_node = current_node.next

		self.head = new_head

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_list()
linked_list.reverse_list()
linked_list.print_list()











