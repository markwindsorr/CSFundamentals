"""
Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value

"""


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Depth-First Search
        
        """
        Depth first search to output all values 
        of the array. Then check if they are equal

        Time Complexity: O(N), where N is the number of nodes in the 
                         given tree

        Space Complexity: O(N)
        
        """
        
        values = []
        
        def dfs(node):
            if node:
                values.append(node.val)
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        # Here, set removes all repeating elements and
        # then we get the length of that collection... it should be 1
        return len(set(values)) ==

    # Recursion

    """
    A tree is univalued if both its children are univalued, plus the root 
    node has the same value as its children

    Time Complexity: O(N), where N is the number of nodes in the given tree.
    Space Complexity: O(H), where H is the height of the given tree.

    """

    def recursion(self, root):

        # Check if left children has the same values
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        # Check if right children has the same values
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        
        return left_correct and right_correct


