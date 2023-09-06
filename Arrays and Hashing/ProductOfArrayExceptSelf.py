class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) #initlizes an array of length input array nums, with each val as 1

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix    #set the index to the prefix
            prefix *= nums[i]  #update prefix so at index 1, prefix will currently hold 1 and then nums[1] = 2 so 1 * 2 = 2
            #so on the next iteration res[3] will hold 2
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):     #want to start at the end for postfix
            res[i] *= postfix     #since we already have the prefix in the res, just multiply postfix to the res[i] so it would be postfix * prefix
            postfix *= nums[i]  #update postfix, same concept as what happen with the prefix but starting from end of nums array
        
        return res
