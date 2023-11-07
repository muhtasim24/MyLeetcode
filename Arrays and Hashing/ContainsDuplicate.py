'''
We are given an integer array nums
if any value appears at least twice
    return True 
else return False 

So we can use a set data structure
if an element thats already in the set appears, return True immediately 
if we can get through the loop, return False

Time Complexity: O(n) for going through entire array
Space Complexity: O(n) for creating a set data structure that can be the size of the input array

'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDups = set()
        for i in nums:
            if i in noDups:
                return True
            else:
                noDups.add(i)
        return False
        
