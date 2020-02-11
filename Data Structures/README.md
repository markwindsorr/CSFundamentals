<h1 align="center">
   :statue_of_liberty:  Data Structures
</h1>

<h3 align="center">
	Organziation, management and storage format that enables access and modification
</h3>

# Arrays

A array is a collection of items stored at contiguous (next to each other) memory locations. The idea is to store multiple items of the same data type together. 

___


# Stacks

A Stack is a linear data structure that follows the Last In First Out (LIFO) order of operations. We can understand a stack by imagining a stack of plates. Usually when setting the table with a stack of plates, you would use the one on top first.

___

# Queues

A Queue is another linear structure that follows the the First In First Out (FIFO) order of operations. We can understand a queue by imagining a line up of people waiting for something. The item (or person) that was in the queue the longest gets processed first.

___

# Linked Lists

A Linked list is a linear data structure where items are not stored at contiguous locations like arrays, but are linked by pointers which are memory addresses within the computer. Each item in which are usually referred to as nodes, contains the data and a reference to the next null. 

The first entry of a linked list is called the head and the last node points to a null reference indicating the end of the list.

___

# Trees

Unlike arrays, linked lists, stacks and queues, a tree is a non-linear data structure that simulates a hierarchical tree structure, with a root value and subtrees of child nodes. 
 
One reason you might want to use trees to store information is that its data is hierarchical in nature, such as a file system on a computer.

## Binary Tree

A tree whose nodes have at most 2 children. We typically the child nodes left and right.

### Traversals

          1
         / \
        2   3
       / \
      4   5


***Inorder Traversal (Left, Root, Right)***

 1. Check if the current node is empty
 2. Traverse the left subtree by recursively calling the in-order traversal function
 3. Visit the root, display the data
 4. Traverse the right subtree by recursively calling the in-order traveral function

4, 2, 5, 1, 3

#### Recursive In Order

 inorder(node)
 	if node == null:
 	    return
 	inorder(node.left)
 	visit(node)
 	inorder(node.right)


 In other words, we keep exploring the left child node until we find null. When we find null, we have reached a leaf node. Then we visit the leaf nodes root, and then we visit the next right child in which we do the same process, exploring the left subtree.

 ***Preorder Traversal (Root, Left, Right)***

 preorder(node)
 	if node == null:
 		return
 	visit(node)
 	preorder(node.left)
 	preorder(node.right)

1. Check if the current node is empty
2. Visit the root node(the current root node)
3. Traverse the left subtree by recursively by calling the preorder function
4. Traverse the right subtree by recursively 











