# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
we are given a binary tree, we have to determine if its a valid Binary Search tree (BST)
valid BST if:
    - all nodes on the left are smaller than parent node
    - all nodes on the right are larger than parent node
    - both left and right subtrees are also BST's

for ex:
        5
    3       7
        4       8
above is not a BST
3 is smaller than 5, that is okay
7 is larger than 5, okay
8 is larger than 5 AND 7
4 is to the left of 7 and smaller than 7, HOWEVER
4 is ALSO on the right of 5 BUT SMALLER THAN 5, this makes it invalid 
there are bounds each node has to follow
the root node can be anything 
has be in between the bounds -infiinty and +infinity
but once we go left, the bounds change 
the node has to be smaller than root but larger than -infinity
        5
    3       7
        4       8
so in this case
going left from 5
bound is -infinity < x < 5, larger than -infinity and smaller than 5
3 fits 
going right, you update the left boundary because it has to be larger than previous node
5 < x < infinity
7 is good
going right to 8
7 < x < infinity
8 fits
however
when we go left from 7, update right boundary
5 < x < 7
4 does not fit

KEY: 
 left < x < right 
 when we go left, update right boundary
 when we go right, update left boundary
 create helper function to pass boundaries
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True #NULL Tree is valid BST
            #if x < left and x > right is not true, invalid BST
            # left < x < right
            # x > left
            # x < right
            # IF NOT TRUE
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and #go left, update right boundary
                    valid(node.right, node.val, right)) #go right, update left boundary

        return valid(root, float("-inf"), float("inf")) # start call with root 
                        #bounds for root are -infinity < root < infinity
