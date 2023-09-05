'''
So we want to have a map that has the num -> index 
we check if target - i is in the map
return [map[target - i], and index of i]
if not in the map 
add it
use the enumerate function to have the index and the value at the same time in the for loop

runtime: O(n)
memory: O(n)

'''




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff in indexMap:
                return [indexMap[diff], index]
            indexMap[number] = index
