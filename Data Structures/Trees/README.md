<h1 align="center">
    :evergreen_tree: Trees
</h1>

<h3 align="center">
	A Learning Repository
</h3>



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

In the case of a binary search tree, in order traversal gives nodes in a non-decreasing order. You can reverse the order of operations to get a non-increasing order

 1. Check if the current node is empty
 2. Traverse the left subtree by recursively calling the in-order traversal function
 3. Visit the root, display the data
 4. Traverse the right subtree by recursively calling the in-order traveral function

4, 2, 5, 1, 3

#### Recursive In Order

```
 inorder(node)
 	if node == null:
 	    return
 	inorder(node.left)
 	visit(node)
 	inorder(node.right)
```

 In other words, we keep exploring the left child node until we find null. When we find null, we have reached a leaf node. Then we visit the leaf nodes root, and then we visit the next right child in which we do the same process, exploring the left subtree.

 ***Preorder Traversal (Root, Left, Right)***

1. Check if the current node is empty
2. Visit the root node(the current root node)
3. Traverse the left subtree by recursively by calling the preorder function
4. Traverse the right subtree by recursively 

1, 2, 4, 5, 3

#### Recursive Pre Order

```
 preorder(node)
    if node == null:
 		return
 	visit(node)
 	preorder(node.left)
 	preorder(node.right)
```

***Postorder Traversal (Left, Right, Root)***

1. Check if the current node is empty
2. Traverse the left subtree by recursively calling the postorder function
3. Traverse the right subtree by recursively calling the postorder function
4. Visit the node

4, 5, 2, 3, 1

```
postorder(node):
	if node == null:
		return
	postorder(node.left)
	postorder(node.right)
	visit(node)
```





