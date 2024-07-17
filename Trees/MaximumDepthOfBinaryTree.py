'''
we are given the root of a binary tree
find the max depth as in find the loongest path from the root to the farthest leaf node
we can do a recursive DFS
DFS will go down a single path till the end and then come up 
we can calcualte the depth as we come up

            3
        9      20
            15.    7
3 = 1 + max(dfs(left), dfs(right))
recursive call and take the max between left or right subtrees
left has no children after 9 so just 1 , right has more children so look at right
20 = 1 + max(dfs(left), dfs(right))
both children of 20 have no other nodes, so depth is 1 for both 
so at 20, depth is 2 because 1 + max(1, 1) = 2
so from 20 going up to 3
we have 3 = 1 + max(1, 2)
            1 is from left subtree (9)
            2 is from right subtree (20 and its children)

Time: O(n)
Space: Height of tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # IF NOT root = if is empty
        # if root = if root is not empty
        if not root: #if root is empty
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
