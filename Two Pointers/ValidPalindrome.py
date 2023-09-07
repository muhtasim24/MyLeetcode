'''
to avoid using extra memeory, we can do everything with the given string and not create a new string

2 pointers 
one at the beginning and one at the end 
left pointer and right pointer
if phrase is a palindrome string(left) will always equal string(right)

if we come across a non-alpha num character continue onto the next character 
either increment the left pointer
or decrement the right pointer

create a alphanum fucntion 
uses ascii values with ord()
if the given character, c 
is alpha num it will be in between the ranges of ord('A') and ord('Z'), ord('a') and ord('z'), ord('0') and ord('9')



'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        #the pointers should never cross each other, only meet in the middle
        while left < right: 
            #check to see if left pointer is at an alpha num char
            while left < right and not self.alphaNum(s[left]):
                left += 1
            #check to see if right pointer is at an alpha num char, if not decrement right
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            
            #both pointers are at alpha num and they should be equal at each instance if they are a palindrome
            if s[left].lower() != s[right].lower():
                return False
            
            #update the pointers 
            left = left + 1     #need to use left to update because what if it was incremented when at a non-alpha num char
            right = right - 1
        
        return True
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
