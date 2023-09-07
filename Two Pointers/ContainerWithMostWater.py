'''
we are calculating area 
area is width X height 
we are given an array of heights 

we use 2 pointers
1 at the very beginning 
1 at the very end to start with the max width

so the width would be the right pointer - left pointer
[1, 8, 6, 2, 5, 4, 8, 3, 7]
 L                       R

 so width is R - L * the minimum height which is 1, because if we choose 7, the water can tip over the shorter height 
 and we would keep track of the max area 

 so to find the max area, we would want to maximize the height 
 so since the left pointer has the lower height, we would shift that,

 shift the pointer with the lower height 

[1, 8, 6, 2, 5, 4, 8, 3, 7]
    L                    R  

area = R - L * min(8, 7)
 = 49
which is actually the answer in this problem
'''



class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(area, result)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return result
