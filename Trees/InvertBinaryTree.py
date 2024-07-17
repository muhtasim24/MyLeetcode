'''
we are given the root of a binary tree, we need to invert it
by Inverting it means to, basically make the left go to the right, and right go to left
Swap left and right 
we can do this with a recursive DFS algo
we visit every single node in the tree,
everytime we vist a node, look at its 2 children,
swap the positions of the children 

Time: O(n) #going through every node

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #if root is NULL
            return None
        
        #swap children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
