'''
we are given an integer array nums and an int val
we have to remove all occurences of val in nums in-place (which means we cant delete it)
we have to return k, which is # of elements that arent val

and for nums, the first k elements, cannot be val
so lets say val = 2, and k = 5, the first 5 elements cannot be val

so how are we going to do this, we can actually use a pointer that we use to change values of 
the values
so we can have the pointer k 
and an iterator i
i will keep going, i wont do anything if it equals val
but if i != val, then we move nums[k] = nums[i]
so this could even mean we set values to the same value in the same index
but then we increment k
at the end we return k, the # of times we increment k, will show us how many values are not val

so ex:
set k = 0, i is the iterator
nums = [0, 1, 2, 2, 3, 0, 4, 2] val = 2
        k
        i
i doesnt equal val, so swap, but stays same
nums = [0, 1, 2, 2, 3, 0, 4, 2] val = 2
           k
           i
swap itself
nums = [0, 1, 2, 2, 3, 0, 4, 2] val = 2
              k  
              i
i is val, so do nothing keep going
nums = [0, 1, 2, 2, 3, 0, 4, 2] val = 2
              k  
                 i
do nothing again
nums = [0, 1, 2, 2, 3, 0, 4, 2] val = 2
              k  
                    i
now i is at 3, which is not val
so make nums[k] = nums[i]
so now we have, 2 become 3

nums = [0, 1, 3, 2, 3, 0, 4, 2] val = 2
                 k  
                       i
    i is at 0, its not val
    so make nums[k] = nums[i]
so now that 2 becomes 0
nums = [0, 1, 3, 0, 3, 0, 4, 2] val = 2
                    k
                          i
    i at 4, not val
    so set nums[k] = nums[i]
    so 3 becomes 4
    nums = [0, 1, 3, 0, 4, 0, 4, 2] val = 2
                           k
                                 i
                    i is at the val, 2, do nothing
                    now we just return k, that was the # of times we set values
                    and notice k = 5, the first 5 elements are not val, 2, anymore
'''



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
