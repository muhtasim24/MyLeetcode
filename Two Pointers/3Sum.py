'''
want 3 # that add up to 0 in a list
cant have duplicate solutions 
 a + b + c = 0
 the value at a can never be the same cause higher chance of creating duplicate solutions 

once u set a, you just use two sum to solve for b and c
so 2 pointers 
if ssum > 0, move r 
if sum < 0, move l

we only have to update one pointer once we find a solutiojn set because our conditions will move the other 

because we dont want the same values in the same position 

so only move the left pointer if it was the same number previosulyt and also make sure it doesnt pass the right poitner


'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #if i is not the first index and a is the same value, just continue to next iteration
            if i > 0 and a == nums[i - 1]:
                continue 
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0: 
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    #update one of the pointers to continue on to find more solution sets
                    left += 1
                    # if the left pointer comes across a value that was already in the position, have to move over to the next value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
