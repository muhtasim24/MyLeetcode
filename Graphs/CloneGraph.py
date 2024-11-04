"""
'''
so we are given a reference to a node in a connected undirected graph
we have to create a deep copy, which is bascially a clone of the graph
We cannot return the same copy but have to return an exact clone of the graph
each node has
 - val
 - list of Nodes that are neighbors connected to the node

so we can use a hashmap to map the old Nodes to the new(copy) nodes
and everytime we create a copy of a node, add to the map
and after that go through the original node's neighbors
for all those neighbors, create a clone if a clone doesnt exist already
how do we know if it doesnt exist already,
we can just check the map
and as we check the neighbors, we will append to the COPY Nodes list of node neighbors

this way we are also getting the connections and the copy nodes neighbors
Time: O(n) = n = Edges + verticies


'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if given empty graph
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            # if the node already has a clone, we just return the clone
            # so we have to check if the clone already exists in the map
            if node in oldToNew:
                return oldToNew[node]
            
            # if clone doesnt exist, create the clone and mapping
            copy = Node(node.val)
            oldToNew[node] = copy

            # go through the original nodes' neighbors to clone them to
            # and them to the list of neighbors for the clone node
            for nei in node.neighbors:
                # run dfs on the neighbors
                # add to the clone list of neighbors
                copy.neighbors.append(dfs(nei))
            
            # return the copy node
            return copy

        return dfs(node)
