# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we are given two binary trees, p and q 
we have to determine if p and q are the same 
they are the same if:
    - idential structure, and nodes have the same value

we can do a recursive dfs
start at the root node, check if theyre the same, if they are 
recursively call the function going left and right

Base Case?
- if both nodes are NULL, thats the same so return True
- if one node is NULL but the other isnt, thats NOT the same, return False
- if both nodes are NOT NULL, but have DIFFERENT values, return False


'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #both nodes are NULL
        if not p and not q:
            return True
        # if one of the nodes is NULL
        # OR, the values are not the same
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))
