'''
Difficulty: EASY
A palindrome is something that reads the same backwards and fowards 
so this can be done using a 2 pointer method
one pointer at the beginning and one at the end 
while left pointer did not pass right pointer 
    if left and right pointer dont equal each other, return False
    increment the pointers as you go
    left += 1
    right -= 1
if finish loop
return True

time complexity : O(n)
space: O(1) no extra data structure
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        toStr = str(x)
        left, right = 0, len(toStr) - 1
        while left < right:
            if toStr[left] != toStr[right]:
                return False
            left += 1
            right -= 1

        return True
