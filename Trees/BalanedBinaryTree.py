'''
we are given a binary tree, we have to determine if it is a balanced binary tree
a tree is balanced if the depth of left and subtrees (height) differ by at most 1 
so the height of one child can only be higher than the other child by 1
if by anymore it is not balanced

so we can run dfs on each node and its children
instead of asking at each node from the top and going down if the tree is balanced 
it will be easier to start at a leaf node and work our way up
this way we visit each node only once

Using Example 1: 
we start at 3, run dfs on both its children 
keep going till we reach lets say 15
run dfs on 15, we'll be at None for both left and right children, so its balanced 
and as we come up from NULL, we bring up the height too 
so at 15 we can check if the differnece of height between left and right are <= 1

so we need to meet 2 conditions for a subtree to be balanced:
 - both left and right have to be balanced 
 - difference of height between left and right <= 1

so 15 is balanced, same for 7.
so at 20
we check if 15 is balanced and 7 is balanced = yes
and we also check if height of 15 - height of 7 <= 1 -> yes cause both heights are 1 

we will pass up [True/False, height] for each node



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
            if not root:
                return [True, 0] #NULL is balanced and has height of 0
            
            #run dfs on both children
            left = dfs(root.left)
            right = dfs(root.right)

            # check if both left and right are balanced
            # and if their heights difference is <= 1
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1 # both conditions will return bools
                        # True or False , both must be true to be balanced

            # in recursive function we want to pass up if balanced, and height
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0] # we just need to return the boolean, True or False if balanced
            
