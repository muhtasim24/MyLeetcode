'''
so we are given the roots of 2 binary trees
we have to figure out if the subRoot is a subTree of root
So subRoot would be a subTree of root IF:
 - subRoot exists within root

how can we do this?
so if it is a subTree that means the same tree exists within the root tree
so we could create a helper function to compare a subtree of root and subRoot
and if its not a subRoot, we can recursivly call our main function on the left / right subtree of root

so we could implement helper function sameTree:
if both are NULL, then they are the same
if they are non NULL, and their values are the same
 - we recursvily call sameTree on both trees left and right children
 - return the result of the recrsvie calls, both left and right sides should be true to be the same

now for our main function
we have to worry about some cases
if subRoot is an empty tree, we can automatically reutnr Ture
because an empty tree is always a subTree of any given tree

However, if our root tree is empty, and our subRoot tree is not empty, that cant happen
the subRoot wouldnt exist in an empty tree

now if their values are the same, we can call sameTree on the root and SubRoot

if they arent, we can rescurivly call our main function on left/right child of root, and pass subRoot

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is empty, we can automatically retunr True
        if not subRoot:
            return True
        # now if above condition fails, as in subRoot is not Empty, but root is, subRoot cant be a subTree of root
        if not root:
            return False
        
        # call sameTree on both roots, to check if they are the sameTree
        # no point of checking if they have same vals to call sameTree, just see if sameTree is true or false
        if self.isSametree(root, subRoot):
            return True

        # if they arent the same val, we can recursively call isSubTree on root's left / right child
        # and only one subTree has to be True, for us to find it 
        # so either left subtree of root has subRoot OR right subTree of root has subRoot as a subTree
        # if not, subRoot does not exist, so instead of AND to compare if its same Tree
        # we do OR to check if the subTree exists within root tree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def isSametree(self, s, t):
        #if both are NULL, they are the same
        if not s and not t:
            return True

        # if both are not empty, and their vals are the same, run sameTree on both children
        if s and t and s.val == t.val:
            return (self.isSametree(s.left, t.left) and
                    self.isSametree(s.right, t.right))

        return False
