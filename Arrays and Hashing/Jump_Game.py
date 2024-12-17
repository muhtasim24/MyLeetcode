'''
we are given an integer array nums. We start at the first index
each element in the array represents max jump we can make at that position
we have to retrun true if we can reach the last index

so to make this easier, we can actually do this in a greedy solution
and start from the end and work our way backwards
our goal post is the last index
and we have to see if we can reach the beginning
g = goal
ex: [2, 3, 1, 1, 4]
                 g
we will iterate reverse
so can the current index + value of the current index >= goal index, yes then we update goal
     0. 1. 2. 3. 4 (indexes)
ex: [2, 3, 1, 1, 4]
              i  g
so at index 3 + 1 (index 3's value) = 4 (which is goal index), so this position can reach the goal
so if we just get to this index, we know we can reach the goal, so really for the next index
we just have to reach index 3 to be able to reach the goal
so we can update our goal to be at this index now, since if we reach here, we can reach the end goal


     0. 1. 2. 3. 4 (indexes)
ex: [2, 3, 1, 1, 4]
           i  g
so can index 2 reach the updated goal,
index 2 + 1 (index 2's value) >= goal??? yes
2 + 1 = 3, which is where the goal currently is 
so that means if we can reach index 2, we can reach index 3, ultiamly means we can reach index 4
since index 3 can reach index 4(goal)
     0. 1. 2. 3. 4 (indexes)
ex: [2, 3, 1, 1, 4]
        i  g
can i(index 1) + nums[i] (3 index 1's value) reach the updtedgoal?
yes 1 + 3 = 4, so we can upadte our goal to be at index 1
     0. 1. 2. 3. 4 (indexes)
ex: [2, 3, 1, 1, 4]
     i  g
can we reach updated goal? 0 + 2 >= 1 yes, so goal = 0, goal is now at the beginning 
so if we reach the end of our iteration and goal's index is 0 that means from the 
end we reached the beginning, if we reach the beginning
that means the beginning can reach the end (actual goal)

but if the goal is anything but 0, that means we did not reach the beignning
thus, the begining cannot reach the goal

Time: O(n) Linear, visited each element of the entire input once
Space: O(1), never created any other data strucutre
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1): #start at last index, decrement by -1, go past 0th index
        # if current index + current value can reach the goal, that means we just need to reach 
        # the current index to reach the goal, so goal can be updated to the current index
            if i + nums[i] >= goal:
                goal = i
        
        # if goal can reach the beginning, as in goal's index will be 0,
        # that means we can reach the end from the beignning so return true
        return True if goal == 0 else False
