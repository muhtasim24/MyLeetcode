'''
we are givne a string array
we need to reverse the string array in place, so in O(1) memory space
to do this we can use 2 pointers
left and right
and just keep swapping while our pointers do not meet

Time: O(n)
Space: O(1)

'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 
        right = len(s) - 1

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -=1

        
