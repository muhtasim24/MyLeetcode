# -------------------------------------- BFS SOLUTION -----------------------------------------'''
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

# -------------------------------------- DFS SOLUTION -----------------------------------------

'''
so we are given a 2d grid
we have to determine the maxArea of islands in the grid
area = # of 1's on an island
we return the maxArea, so the most # of 1's we see on one island
islands are connected horzontially and vertically

so we can go through the grid
everytime we encounter a 1, we can run dfs on the position

1's ARE INTS NOT STRINGS IN THIS PROBLEM

AND A DFS SOLUTION
dont need queue
if grid[r][c] == 1
run dfs on it 
and within the function run dfs recrusvily on all 4 directions and add in return

have a check to see if not within bounds, if already visited, or if position is a 0
just return 0 
but if not we can just add node to visit set, and run dfs on all 4 direciton while returnig our area

and we compare the max between the dfs call and previous maxArea
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # get the dimensions
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0

        #bfs function that will return # of 1's on a given island
        def dfs(r,c):
            # if row and col NOT WITHIN BOUNDS, and the node has already been visited
            # return 0
            if (r < 0 or r == rows or c < 0 or c == cols or
                (r, c) in visit or grid[r][c] == 0):
                return 0
            
            # but if its a good position we can add it to visited
            # and run dfs on it within all 4 directions
            visit.add((r,c))
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))


        # go through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))

        return area
