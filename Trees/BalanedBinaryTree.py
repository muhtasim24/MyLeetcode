'''
We are given a binary tree
We have to determine if its balanced
A tree is balanced if the left and right subtrees have a difference in height of max 1
So we could go to every node and check the subtrees and their subtrees to see if its balanced

But we could work our way up from the very bottom 
use a recursive dfs 
on our way up we tell the parent node, if that child was balanced and if the subtrees diff by max 1
the height difference has to be less than or equal to 1
and we will also return our way up if its balanced 

Base case, will be a leaf node (no children). Leaf node is balanced, and has 0 height

Time: O(n)
Memory: Height of tree

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root: #if leaf node
                return [True, 0] #will be returning Balanced, and height

            left = dfs(root.left)
            right = dfs(root.right)
            #boolean that holds whether we are balanced
            # node is balanced IF
                # BOTH children are balanced, first index is True or False if it is balanced
                # AND heights of children are <= 1, second index is the height
            balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0] #need to do [0] cause we want only the boolean when returning if the entire
        #tree is balanced, not the height at [1]
