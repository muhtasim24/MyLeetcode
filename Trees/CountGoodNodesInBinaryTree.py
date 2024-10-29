'''
we are given the root of a binary tree
we have to find all the good nodes in the tree
a good node is a node:
- from the path from the root to the Node, there are no nodes with a value greater than X

can we do this with BFS, 

im assumign the root node is always a good node
so how can we do this

                3
         1.          4
     3           1      5

so we start at 3, thats already a good node
initlilize queue with 3
right now the max is 3, we keep track of the max = 3
then add its neighbors, 1 and 4
when we look at 1, compare to max, 
if node > max:
    good_node += 1
else just keep going
now that was popped
we look at the right child 4, max is still 3
if node(4) > max(3):
    good_node += 1 TRUE
now we add their children
new max for right side is 4, but for left side its still 3
so maybe when we put nodes into our queue, we also add in the max

so [node, maxVal]
if node >= maxVal: so node is larger so we can update maxVal to node
    good_nodes += 1
    maxVal = node
#add neighbors
node.left, maxVal
node.right, maxVal

so you cant put in multiple values in with a queue
so we can actually do a recursive preOrder Traversal DFS

we can create a dfs helper fucntoin, pass in the node, and current maxVal that we were talking about
and res = 1, if node.val > maxVal
and update the maxVal
if not res = 0

after we handle that, we recursively call dfs on the left and right subtrees
and return res + left + right
this should return and result of all the good nodes in both subtrees


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if empty, no nodes, so 0
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res = 1
                maxVal = node.val
            else:
                res = 0
            
            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)
        
            return res + left + right
    
        return dfs(root, root.val)
