# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            #get the heights of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right) #Diameter = 2 + height of left + height of right

            return 1 + max(left, right) #this gives us the height as we work our way up the nodes in the tree
        
        dfs(root)
        return res[0]
