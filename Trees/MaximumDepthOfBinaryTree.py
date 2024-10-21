'''
RECURSIVE DFS SOLTUION
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



'''
ITERATIVE BFS SOLUTION
we are given the root of a binary tree, we have to return its max depth
so basically the max level the tree gets to
so with that we can do an iterative BFS solution:
if root is NULL, we return 0
and in a BFS solution we use a queue, because we go level by level
so at each level, we iterate through the entire queue, and then add its children as we go
once we are done iterating through that level, we can increment the # of levels

so we will be going through the queue at each level
we will have the length of queue before we add any of children so we know to only go through the nodes
at the current level



'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root]) #initilize with the root
        level = 0

        # while the q is not empty
        while q:

            for i in range(len(q)): #this creates a snapshot of the current q before we add in new nodes
            # this way we only go through the nodes at the current level before going on to the next
                node = q.popleft()
                # make sure the children of this node are not NULL to append to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # after we have gone through that level, increment level
            level += 1
        return level

'''
ITERATIVE DFS SOLUTION
given the root of the tree, we are to return its max depth
for a dfs solution, we can use a stack
at each node, we will append the nodes children and their depth

the stack will go use the node that was last pushed
and if no new nodes were added, it will go the next one on stack 
but if new nodes are added, the stack will go through that node
LIFO, LAST IN FIRST OUT


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [[root, 1]] #initilize with the root
        res = 0

        #go through every node in the stack
        while stack:
            node, depth = stack.pop() # we have 2 values for each node in the stack, the val and its depth

            # check if our node is non NULL, not NULL
            if node:
                #if its not NULL, add its children
                # see if the depth of this node, is higher than the current depth
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

            # now if the node is NULL, we just go through it and return 
        return res
