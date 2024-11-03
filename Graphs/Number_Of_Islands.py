'''
We are given a 2d grid, which has '1's (land) and '0's(water)
we have to return the # of islands
An island is surrounded by water and can be connected by other pieces of land 

so if 1's are connected in the directions of horizontally or verticlaly, they are not 2 different isalnds
they are counted as 1 island
so we only increment the # of islands if we reach a '1' that has not been visited, 
and we check that piees land's neighbors to increment that land with the entire island not just that
point of the land

[1 1 1 0 0]
[1 1 0 0 0]
[1 0 0 0 0]
[0 0 0 1 1]
We have 2 islands in this grid
we start at the first piece of land (1) check all directions, up down left right
if in those directions there is a 1, we run bfs on that too and mark it visited
if we encounter a '0' we do nothing
so we can run BFS, have a queue, and a visited set to explore adjacent nodes and to mark nodes we 
already visited so we dont increment # of islands when they are connected to each other


'''



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if grid is empty return 0
        if not grid:
            return 0

        # get the dimensions
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        #bfs function
        # takes in row and column
        def bfs(r,c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))

            while queue: # go through the queue while its not empty
                row, col = queue.popleft() #explore the node we are at

                directions = [[1,0], [-1, 0], [0, 1], [0, -1]] #all 4 directions
            # so for each direction, we want to check if there is a neighboring 1
            # we only care to explore those directions
            # if that direction is within bounds
            # if that direction, point is a '1'
            # and if that point in that direction was NOT already visited
                for dr, dc in directions:
                    if ((row + dr) in range(rows) and 
                    (col + dc) in range(cols) and
                    grid[row + dr][col + dc] == '1' and
                    (row + dr, col + dc) not in visit):
                        #explore the node, and mark it visited
                        visit.add((row+dr, col+dc))
                        queue.append((row+dr, col+dc))

        # so we call bfs on a node 
        # Go though the grid
        for r in range(rows):
            for c in range(cols):
                # run bfs if we have a 1 thats not visited
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
