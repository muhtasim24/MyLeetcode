'''
we are given the string s
we have to reverse the each string but keep the order of the strings and the white spaces

so we could go through every string in s
and for each index, each string we want to reverse that string
but strings are immutable
so we will create a new string, and append from the end to the start
we could then create a new array, append the newStrings to it as we go
and join the new array with a space delmiter

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        
        for word in words:
            newStr = ""
            for s in range(len(word)-1, -1, -1):
                newStr += word[s]
            res.append(newStr)
        
        return ' '.join(res)
