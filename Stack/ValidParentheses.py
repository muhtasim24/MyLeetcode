'''
We are given a string s, with parenthesis
we have to determine if a string is valid
they are only valid, if they are closed in the correct order and with their correct counter part

we can have a map that matches the closing brackets to their correct opening bracket
ex: 
[](){} this is valid
([)] not valid, not closed in correct order 

(((()))) , this is valid, we have 4 open and 4 closing 
so we can do this by having a stack
if our character is a opening bracket, we can keep adding to the stack

it is only okay to have a closing bracket if stack is not empty AND top of the stack 
matches its value

if top of the stack matches map[character]
if it does match, we can pop from stack, if not return false right there

by the end our stack will be empty if our string is valid and everythign was closed properly
and stack is not empty return false since invalid string

Time: O(n) -> going through input once
Space: O(n) -> for stack
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]" : "[" , "}" : "{", ")" : "("}
            #every key in the map is a closing bracket
        for c in s:
            if c in closeToOpen: # if the character is a closing bracket
                if stack and stack[-1] == closeToOpen[c]: 
                    # if stack is not empty AND top of the stack
                    # is a opening bracket that is the value
                    # of the key which is the closing bracket
                    # remove from stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        #if stack means if stack is not empty
        # if not stack means if stack is empty
