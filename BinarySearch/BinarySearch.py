'''
we are given array nums in sorted ascending order and an int target
we search if target is in nums, if it is return its index
if not return -1

simple run binary search
have 2 pointers 
L and R
find the mid way point
nums = [-1,0,3,5,9,12], target = 9
[-1   0   3   5   9   12]
 L                     R
binary search always runs in O(log n) because we are always cutting the number of elements we look at
by half
so to find mid way point, L + R / 2
[-1   0   3   5   9   12] target = 9
 L        M            R

now compare Midway point to the target. 
mid is not equal to the target, check if it is larger or smaller
if the mid way point is larger than the target that means 
we need to look at all numbers smaller than mid
if mid point is smaller than the target that means
we need to look at all numbers larger than mid

so to find mid way point, L + R / 2
[-1   0   3   5   9   12] target = 9
 X    X    X  L   M      R

Time: O(log n)
Space: O(1)
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:    #we do <= in the case we have an array of 1, [1],
                                #L and R would be both at that one element
            mid = (left + right) // 2 # we need to do // becasue doing / creates a float
                # // gives us a single int, no decimals

            if nums[mid] > target: #mid too large, look at smaller numbers
                right = mid - 1
            elif nums[mid] < target: #mid too small, look at larger numbers
                left = mid + 1
            else:
                return mid
        return -1 #if never found

        
