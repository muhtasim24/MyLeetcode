'''
we are given an integer array nums in sorted non-decreasing order
we have to remove the duplicates in place, so that the unique elements appear once
First k elements contain the unique elements in the order they were presented
we have to return k, so basically the number of elements that are distinct
and in nums, the first k elements have to be distinct we cnanot have duplicates

so how can we do this?
we have a pointer k, and an iterator i
we can have a set, that marks our duplicates
so we come to a element, its new, add to our set

set = []
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
        k
        i
start at i, i is 0, add 0 to set
increment k
set = [0]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
           k
           i
i,0, is already in the set, so keep k where it is and move on to next with i
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
           k
              i
i is not in the set, so add that to the set
set nums[k] = nums[i], and increment k
so the 2nd 0 becomes 1
set = [0, 1]
nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4] 
              k
                 i
i, 1, is in set, we dont do anything
set = [0, 1]
nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4] 
              k
                    i
    do nothing, already in set
set = [0, 1]
nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4] 
              k
                       i
    i, 2, is not in set, so set nums[k] = nums[i]
    and increment k
so 1 becomes 2, then we increment k
set = [0, 1, 2]
nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4] 
                 k
                          i
                          nothing
set = [0, 1, 2]
nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4] 
                 k
                             i
        i, 3, not in set, so add to set,
        set nums[k] = nums[i]
        so 1 becomes 3, and increment k
set = [0, 1, 2, 3]
nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4] 
                    k
                                 i
                        nothing here, i already in set
set = [0, 1, 2, 3]
nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4] 
                    k
                                   i
                            i, 4, not in set, add it
                            set nums[k] = nums[i]
                            1 becomes 4
                            increment k
set = [0, 1, 2, 3, 4]
nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] 
                       k
                                   i
                                   we return k
                    i is at the end, so notice first k, 5, elements are all unique
                                



'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        noDups = set()

        for i in range(len(nums)):
            #dont do anything if already seen
            # but if not seen, set nums[k] = nums[i]
            # incremnt k, and of course add to set
            if nums[i] not in noDups:
                noDups.add(nums[i])
                nums[k] = nums[i]
                k += 1
        return k
