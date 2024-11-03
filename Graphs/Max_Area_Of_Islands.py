# BFS SOLUTION
'''
so we are given a 2d grid
we have to determine the maxArea of islands in the grid
area = # of 1's on an island
we return the maxArea, so the most # of 1's we see on one island
islands are connected horzontially and vertically

so we can go through the grid
everytime we encounter a 1, we can run bfs on the position

in our bfs function
if all directions are in bounds and not visited already
we can return the number of 1's on that island

and after going through all 1's on the island
we can maxArea = max(area, maxArea) #compare the area of the island we just computed and orignal max


'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # get the dimensions
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        #bfs function that will return # of 1's on a given island
        def bfs(r,c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            area = 0
        
            while queue: 
                row, col = queue.popleft()
                area += 1
                print(area)

                directions = [[1,0], [-1, 0], [0, 1], [0, -1]] #all directions
# go through each direction
# only add node to the queue
# IF:
#  - position is valid, within bounds
# - position is a '1'
# - not in visit set already
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        visit.add((r,c))
                        queue.append((r,c))

            return area


        # go through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    print("DO I REACHRE")
                    area = bfs(r,c) 
                    print(area)
                    maxArea = max(area, maxArea)

        return maxArea
