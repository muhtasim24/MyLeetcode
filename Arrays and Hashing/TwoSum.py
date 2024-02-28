'''
we are given an array of ints, nums and a target
return the indices of the 2 numbers that add up to the target
only one solution

create a hashmap
we are going to map the element to an index 
since there is only 1 solution and we cant use the same element twice
we want to solve this in one pass 
as we are going through the input array, we are going to be checking for diff = target - element in the hashmap
if the diff exists, return the index of current element and index of difference, which can be easily accessed through the map

if it the difference doesnt exist, just add map[element] = index


'''



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        #element to index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indexMap:
                return [i, indexMap[diff]]
            indexMap[n] = i
            
        
