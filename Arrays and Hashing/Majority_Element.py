# Logical Solution
'''
so we are given the array of nums of size n
we have to return the majority element
majority element is the element that appears more than n/2 times

so lets say we have n = 4
[1, 4, 3, 2, 2] we sort this array
[1, 2, 2, 3, 4] 4/2 = 2, so we get the array[2] inde that gives us 2
which is correct 2 appears 2

how about n = 7
[1, 1, 1, 3, 5, 6, 7] we sorted. 7 / 2 = 3.5 floor it is 3, always need to floor it, we deciamls not floats
so we can just return the index of n//2 which gives us 3, we do // to floor the diviision and round down

that gives us 3
nums[3] = 1, which is correct
Sorting: O(n log n)
So time Complexity: O(n log n)


'''



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n // 2]

# Using hashmap techniques to get the max from the value and retrieve the key
'''
we are given an array nums of size n
we have to return the majority element

majoirty element:
- appears more than n/2 times
so 
nums = [3, 2, 3] n = 3
n/2 = 1.5
majiryt element is 3, it appears 2 > 1.5
what if there are multiple numbers that appear more than n/2 numbers if thats even possible

what if i just create a hashmap with element : count of element 
and take the max of the hashmap, wouldnt that work too


'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        # i have a map, that gives me element : # of that element
        # have to return the element that appears the most
        return max(count, key = count.get)

        
        
        
