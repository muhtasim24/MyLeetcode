'''
we are given an mxn grid that borders pacific and atlantic ocean
The top and left edges border Pacific Ocean
the bottom and right edges border Atlantic Ocean
we have to find the positions in the grid that can flow to both oceans

each position has a height
water can flow to a cell if the neighboring cell's 
height is less than or equal to the current cell's height

        Pacific Ocean
        [1 | 2 | 2 | 3 | 5 ]
Pacifc  [3 | 2 | 3 | 4 | 4 ] Atlantic Ocean
Ocean   [2 | 4 | 5 | 3 | 1 ]
        [6 | 7 | 1 | 4 | 5 ]
        [5 | 1 | 1 | 2 | 4 ]
            Atlantic Ocean
so to this more efficient, we can start from the ocean and see what cells we can flow to
since we are going the opposite direction, we can flow to cells that have a higher height
if their neighbor is lower then we cannot go to it
we can have 2 sets, one for pacific ocean and one for atlantic ocean
we run dfs on the top edge for the pacific ocean
run dfs on the bottom edge for the atlantic ocean
run dfs on the left edge for the pacific ocean
run dfs on the right edge for the atlantic ocean

as we run dfs on the cell, run dfs on the neighrboring nodes as well
passing in the row, column, ocean set, previous Height(to make sure we can flow to it)
we can flow to neighrboing node if their height is greater, so if less we cant flow
once we finish adding the positions to both sets

we will go through every position in the grid
if a position is in both ocean sets, then that positon can flow to both oceans
and we can append that position to our result 


'''



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        #dfs function to go through neighboring cells
        #we cannot flow to neighboring cell IF:
        # - already visited
        # - not in bounds
        # - if their height is less than the height we are currently at
        # else, run dfs on all 4 directions
        #taking in row,column, ocean set, previous Height
        def dfs(r, c, visit, prevHeight):
            if ( (r,c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight): 
                return
            #else we can explore it, and all neighboring cells
            visit.add((r,c))
            # run dfs on all 4 directions, passing in same ocean set
            # and passing in new current height
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        #Go through the top and bottom rows
        # which means every single column in the first row, and very last row
        for c in range(COLS):
            # first row, bordering Pacific Ocean
            dfs(0, c, pac, heights[0][c])
            #last row, bordering Atlantic Ocean
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        #Go through the left and right columns 
        # which means every single row in the first column, and very last column
        for r in range(ROWS):
            # left edge, first column, bordering Pacific Ocean
            dfs(r, 0, pac, heights[r][0])
            #right edge, last column, bordering atlantic OCean
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # after we fill both sets
        # we can go through each position
        # if a positon is in both sets, it can flow to both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
