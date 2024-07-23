# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we are given a Binary Tree, we have to traverse the tree left to right, level by level
Traversing level by level is BFS (Breadth First Search)
We will need a queue
Each level is a sublist
at the end, all sublists are in one list
We will append the root to the queue before iterating through the queue to initilize it
3
9 20
15 7
When we pop from the left of the queue, we will append the children of the node
We will append to the sublist, by the length of the queue before appending the children
That way, we will only append to the sublist for that level
Then when we append the children, we are going to the next level
Time: O(n)
Memory: O(n)

'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q) #gets the length of the queue at the current level
            level = [] #need the sublist
            for i in range(qLen): 
                node = q.popleft()
                #make sure the node is not NULL
                if node:
                    #append the node to the level
                    level.append(node.val) #get the val of the node
                    # add the children of the node to the queue
                    q.append(node.left)
                    q.append(node.right)
            #make sure list level is not empty, we dont want to add empty lists to our list
            if level: 
                res.append(level)
        return res
