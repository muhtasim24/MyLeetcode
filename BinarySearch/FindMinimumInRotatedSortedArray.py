'''
we are given an array of length n, that is sorted and rotated between 1 to n times 
if its rotated, there are 2 sorted portions in the array
a left sorted portion and a right sorted portion
when rotating, the end right values go to the beginning of the left side
[3, 4, 5, 1, 2]
notice how 3,4,5 are sorted
and 1, 2 are sorted
we have to find the min value
we can run binary search
[3,    4,  5,     1   , 2]
 L.        M            R

 if the middle value is a part of the left sorted portion, that means and 
 since all values from the right goes to the left, all values in the left is always larger
 than all values in the right sorted portion

 so how do we know if its a part of the left sorted protion, 
 5 >= 3, left sorted
 if midway is larger than the leftmost, then that means its a part of the left sorted
 so we would check the right side

 but lets say M is in the right sorted portion, 
 lets say M was at 1,
 [3,    4,  5,     1   , 2]
 L.               M      R
 1 >= 3, not true, so we check left, because every number after M to the right is larger 
 and yes some values to the left will be larger but there can also be the smallest value
 check the min at each time

 The conditions we have to follow:
 if nums[M] >= nums[L]: #if this is true, it means we are in the left sorted portion, so check right
    search right
any other case:
    search left

 Time: O(log n) binary search
 Space: O(1)



'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            #if we come across a subarray where the leftmost value is the min, update res
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                #break from the loop
                break
            
            mid = (left + right) // 2
            #before doing anything, see if the mid is smaller than res
            # keep track of it 
            res = min(res, nums[mid])
            #search right if mid is a part of left sorted portion, search left otherwise
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res
