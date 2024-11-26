'''
so we are given an integer array nums
we want to rotate the array to the right by k steps, 
so lets say we have [1, 2, 3, 4, 5, 6, 7] k = 3
so the last 3 elements of nums will be pushed to the right, bringing it to the front
[5, 6, 7, 1, 2, 3, 4]
so how can we do this in place
an easy approach, is to create a new array that has the same length of nums

make the changes in this array, and then copy the values into nums indexes
so res=[]
we will iterate through nums
lets say k = 2 , nums = [1,2,3,4,5] we want to get [4,5, 1, 2, 3]
so that means we are pushing each index by 2
so i + k(2)
so that will work for the first few indexes
nums[0], nums[1], nums[2], since we have a length of 5 and last index being 4
nums[0] = 1 and when we add 2 to the index we will be at index 2
but lets say for index for index 3 and on
nums[3 + 2] = nums[5] there isnt a 5th index, so that would give us an error
what we could do is use a modulo operator
length of nums is 5, so we can divide our index we get when we add 2, by it
so 3 + 2 mod 5 = 5 mod 5 = 0 and thats exaclty where we want our nums[3] = 4 to go, to the 0th index
and same for 4 + 2 mod 5 = 1
we will actually use this for every index and it works
nums[i + k mod len(nums)] , gives us where we want our value to be in the new res array

and then we can just iterate through nums index, and set the values from res

Space: O(n) for creating new array
Time: O(n)

'''



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums) #create a new list, we will use to do the computation
        # and the copy the values to the correct index into nums
        for i in range(len(nums)):
            res[(i + k) % len(nums)] = nums[i]
        
        print(res)
        for i in range(len(nums)):
            nums[i] = res[i]

