'''
we are given an integer array, nums
each element represents the max jump it game make from the index
we have to figure out that minimum number of jumps to reach the end 
we can assume every input array can reach the end

ex:
ex: 
[2, 3, 1, 1, 4]
    _ _________
    1    2
    ____  _.  _
     1.   2.  3    
we can either do this approach, but we want the smallest number of jumps to reach the end 
so output would be 2

so to do this we can use pointers, Left and right to create windows
Left/Right will start at index 0

[2, 3, 1, 1, 4] so starting at the 0th index, we can make a jump of 2 or less
   |_____|      so our window is between index 1 and 2, values 3 and 1
in this window, we want to see the furthest we can go
so in this window we can either make a jump of 3 or less, or a jump of 1
we want the furthest to be the end of the our next window
the start of the next window will be the next index of the end of our current window

[2, 3, 1, 1, 4] so starting at the 0th index, we can make a jump of 2 or less
|_| |___||___|
     1.    2
so in this window we reached the end, you can see it took us 2 jumps to get here
once our R pointer reaches the end, we can stop counting 
everytime we create a new window, we can count that as a jump

from index 0, 2
the window of jumps we can make is between 3 and 1
and from that window the furthest we can go is taking max jjjump of 3, or taking 1 jump
so that is our new window
our new window contains the last index, so our right pointer has reached the end
that means we can take the number of windows we created as number of jumps
so basically everytime we create new window, update our result

Time: O(n)

'''



class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        # we will keep creating windows, till the end of a window(right pointer) is the last index,
        while right < len(nums) - 1:
            farthest = 0 # this will determine the farthest we can go from our current window
            # we will loop through our current window
            # we want to find the furthest index we can reach 
            # by using current index + current index's value
            # do that for every value within the window
            # and keep track of the max index we can reach
            for i in range(left, right + 1): # r + 1 since its not including last parameter
                farthest = max(farthest, i + nums[i])
            # once we have the furthest index we can reach, we can create new window
            # left will go to the pointer right after the end of our current window
            left = right + 1
            # right pointer will go the furthest index we can reach
            right = farthest
            #and since we just created a new window, we can update number of jumps
            res += 1
        # by the end, our window will contain the last index
        # so the number of times we've created new windows
        # we have updated number of jumps needed to get to that window
        # so we can return our result
        return res
