'''
we are given an mXn matrix board contianing 'X's and 'O's
we have to capture the regions that are surronunded:
if an 'O' is surrounded by 'X's in all 4 directions, it is marked captured and we turn it into an X

so to make this problem simpler we can do Reverse Thinking!!

the problem is telling us to find the surrounded regions 
so instead lets capture everything except the unsurrounded region

Ex:
 X X X X        X X X X
 X O O X        X X X X
 X X O X    ->  X X X X
 X O X X        X O X X

so notice how the bottom O never changes into an X, its become its on the border/edge and has no X
at the bottom
to be cpatured 'O' must be surrounded by 'X' in all 4 directions
so we can capture the 'O's that are unsurrounded first
and we are 100% if we are on the border and come across a 0, it is unsurronded
so we can go through every postion on the border, if we come across a 'O' run dfs on that cell
and for those 'O's turn into T to say it is unsurrounded, serve as a temp variable

then we go just do nested loop going through every positon in the board
for the left over 'O's we can just turn them into X's because we already marked the unsurrouneded O's

then once more do a nested loop going through every positon in the board
to turn the Temp variable, T's back into O's

Time Complexity: O(n X M) -> dimensions of the board
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        #return IF:
        # - not within bounds
        # - not a O, this is used to mark unsurrounding regions as T
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
            board[r][c] != 'O'):
                return 
            board[r][c] = "T"
            #run dfs on all 4 directions from the node we found that is unsurrounding
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        # we want to run dfs on only the border positions and if its an O
        # turn O -> T
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and 
                    r in [0, ROWS - 1] or
                    c in [0, COLS - 1]):
                    capture(r,c)
        
        # now go through every postion in the grid
        # for the leftover "O's that are surrounded and we can turn them into X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # now to turn back all the temp variables, T, that are unsurrounded regions
        # back into O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
