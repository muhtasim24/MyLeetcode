'''
so we are given the root of a binary tree, we have to return the length of the diameter of the tree
diameter: length between the longest path between any 2 nodes, does not need to pass through the root

so we can do a recursive dfs on this
keep track of our longest in a res global variable outside of our recursive helper dfs function

for each node we are going to run dfs on its left and right child 
once we reach the leaf node, on our way up we will return the height from the child node from both left and right
at our parent node we will then compute the diameter, 
which is the size of the left subtree + right subtree

in our recrusive function we are return the height

        1
     /.   |
     2.   3
 /   |.  /  |
 4.  5.  6. 7

 so lets say at 4 and 5, we go up returning 1 for each node cause thats the height 
 at our parent node 2, we calculate the diameter, which is left + right = 1 + 1 = 2

 and we return our height to next upper node
same thing for 6 and 7
so at parent node 1, we take the hieght of the left subtree and height of right subtree
which would both be 2
so 2 + 2 = 4, would be our diameter
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            # if root empty, return 0
            if not root:
                return 0

            # run dfs on both children
            left = dfs(root.left)
            right = dfs(root.right) 

            self.res = max(self.res, left + right) #calculate the diameter at parent node
            #return the height 
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
