# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
we are given a binary tree, we have to return the # of nodes that are good nodes
good nodes are for example:
    on the path from root to the node itself, there are no nodes before the current node that are larger
    than the node we are currently at
    As in, the node we are currently at has to be equal to the largest, or the largest node 
    we've seen on the path so far

        3
    1      4
  3      1   5

the root node is always a good node, since its the start of the path
4 is a good node because on the path, there are no nodes larger than 4
1 is NOT a good node on both sides, because 3 is larger than 1, and 4 is larger than 1

so we can do a recursive DFS, preorder traversal
create a helper function that will let us pass the node, and max Node val we've encountered so far
if currnet node >= to maxVal, then res =1 else 0
run dfs on left children and then run dfs on right children
'''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal) #keep track of largest node we've seen on the path
            res += dfs(node.left, maxVal) #dfs on the left, add # of good nodes returned to res
            res += dfs(node.right, maxVal) #dfs on the right, add to # of good nodes returned to res

            return res
        
        return dfs(root, root.val)
