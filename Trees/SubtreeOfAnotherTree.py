'''
given 2 binary trees, root and subRoot
We have to determine if subRoot is a subTree of root
this question kind of builds off SameTree problem

We can recursively solve this with DFS,
we can compare subtrees of root to subRoot(T)

we can build a helper fucntion to compare the subtrees
if the subtrees are not the same, we can just check the left or right subtrees of the root tree (S)

Edge Cases:
if T (subroot) is NULL, we can return True because a NULL Tree is still a subtree of a tree
however if root is NULL, T can never be a subtree of NULL


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subRoot is empty, that can be a subTree of root, so its true
        if not subRoot:
            return True
        #however, if root is empty, subRoot can never be a subtree of the root
        if not root:
            return False
        
        #if they root and subRoot are the same, return True, we found the subtree
        if self.sameTree(root, subRoot):
            return True
        
        #if we didnt find the subtree, we can check the Left subtree and Right SubTree of the root
        return (self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot))
        
    
    def sameTree(self, s, t):
        # if both nodes are NULL, return True
        if not s and not t:
            return True
        
        #if both are not empty and they have the same value
        # check their children
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                self.sameTree(s.right, t.right))

        # if the above statements never execute then the tree is not the same        
        return False
        
