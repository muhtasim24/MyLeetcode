# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
we are given a binary tree, we are told we want to see the nodes from a person that is on the right side
from top to bottom
this would make you to think to continously take the right child, however, if we have a tree like:
    1
2.     3
  5.     4
    7
the 7 would be visible too from the person watching from right side 
so its better to look at this problem as, taking in the rightmost values in each level
we have 1
3 is rightmost
4 is rightmost
and 7 is the only node so that is rightmost in the last level
we want to traverse level by level, left to right
So can use BFS algorithm
we will append the children before popping from the queue 
we will have the length of the queue at the current level
iterate that many times, pop from the left that many times
as we are popping we will have a variable, rightSide that will continously update
and by the end of iterating through the length of the queue, rightSide will be the value of the last pop
as in the last pop is the last value in the level, in the rightmost side in that level

'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            rightSide = None #var to track rightmost value
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft() #pops from leftside of queue
                # if node is not NULL
                if node:
                    #update rightSide as we pop, by the end rightSide will have rightMost val
                    rightSide = node
                    #append its children
                    q.append(node.left)
                    q.append(node.right)
            # we only want to append non NULL vals to result
            if rightSide:
                res.append(rightSide.val)
        return res
        
