'''
Understand:

remove all non-alphanum characters
have 2 pointers one at the beginning of the string and one at the end 
for i in str:
if beginPointer != endPointer:
    return False
else:
    update beginPointer
    update endPointer 
return True



'''



class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True 
        
        newStr = ""
        
        for i in s:
            if i.isalnum():
                newStr = newStr + i
        
        beginPointer = newStr[0]
        endPointer = newStr[-1]
        
        for i in newStr.lower():
            if beginPointer != endPointer:
                return False
            beginPointer = newStr[0 + 1]
            endPointer = newStr[-1 - 1]
        return True
        
        
