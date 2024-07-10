'''
we are given a sorted array that has been rotated
so we have 2 sorted portions
we have to find the target
so we have a few conditions
[4,5,6,7,0,1,2]  , target = 0
     M
if our midway point is in the left sorted portion,
    if our target is less than mid, we can search left or right but we cant do both
        how do we decide 
    if we look at our leftmost value,
    if target is larger than leftmost value, we have to search left
    because target is less than mid, but larger than smallest val in that sorted

    SO if target is less than mid and larger than left most val, search left
    but if target is larger than mid and smaller than leftmost val, search right
    cause there could be numbers still larger to the right, like the 7

[4,5,6,7,0,1,2]  , target = 0
           M
lets say our target is in the right sorted portion, 
if target is larger than mid, we can search right or left
how do we decide:
if target is larger than the rightmost val, then we check left
but if target is smaller than mid, we can only check left

if target is larger than mid, but smaller than rightmost val, we can only search right
'''



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            #left sorted portion, mid is larger than left
            if nums[mid] >= nums[left]:
                #if target is smaller than mid, we search right or left
                # we go right if target is larger than mid, OR smaller than leftmost val
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                #we search left if our target is less than mid, but larger than leftmost val
                else:
                    right = mid - 1
            #right sorted portion
            else:
                # if target is smaller than mid OR larger than rightmost value,
                # we search left,
                #target is larger than mid, we can check right or left
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                # if target is less than rightmost val, we search right
                else:
                    left = mid + 1
        return -1
