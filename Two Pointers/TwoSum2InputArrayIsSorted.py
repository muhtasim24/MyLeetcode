'''
the numbers are in ascending order
so the highest numbers are on the right 

so we can start off with 2 pointers, one at the beginnning and end 
[2, 7, 11, 15]    target = 9
L           R
2 + 15 is 17 
so l + r > target
we have to lower R
[2, 7, 11, 15]
 L     R      

 2 + 11 = 13
 l +  r > target
 we have to lower r 

[2, 7, 11, 15]
 L  R

2 + 7 = 9



'''




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else: 
                return [left + 1, right + 1]   #we have to add 1 to both because array is 1 - indexed
            
            
