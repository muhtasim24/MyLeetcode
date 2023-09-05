'''
Understand: If any element appears more than once, return true,
otherwise return false 

Match: 
Set, Loop over array

Plan: 
Initlize a hashset 
Iterate through the array
If element already in hashset, return true 
Otherwise, add to hashset
return false if gets through loop
'''

class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        hashset = set()
        for element in nums: 
            if element in hashset: 
                return True
            else: 
                hashset.add(element)
        return False
    
