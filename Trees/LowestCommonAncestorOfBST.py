# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
we are given a BST and 2 nodes p and q
we have to find the Lowest Common Ancestor (basically parent)
p and q have to be desendants of the LCA
Finding the lowest parent that is the ancestor of BOTH p and q
the root is the ancestor of all nodes
There are 2 cases:
if both p and q larger than the node we are at:
    we search the right child
if both p and q smaller than the node we are at:
    we search the left child

but if p is larger than node, and q is smaller that node
OR
if q is larger, and p is smaller than node:
    there is a split
Where that split occurs is the LCA of both p and q
Because in that split:
        6
       /. |
      2.   8
     / |  /. |
    0. 4  7. 9 
    0  4. 
p = 2, q = 8, they split at the root, if q is in the right tree, it can never be a descendant of the left tree
vice versa with the left tree and q
If our nodes, p or q is ever the root, the root is the only ancesotr 
The ROOT CAN NEVER BE A DESENDANT OF ANY OF THE NODES BELOW
a node can be an ancestor of its self
Time: O(log n) since we are only looking at one node at each level


'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            #if both p and q larger, search right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            #if both p and q smaller, search left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            #else, we reached a split, OR we reached either p or q
            else:
                return cur
