'''
we are given a string s, need to keep track of the longest substring 
no duplicates
so for no dups we can use a set
we need the sliding window tecnique for substrings 

initlize charSet = set()
and left pointer 

since we are consistently moving the Right pointer, we can just use that as the iterator 

in a loop for right in range(len(s)):

if we come across duplicates we should remove vals from the set from the left pointer
so update the left pointer until no dups 
AND remove from set until no DUPS
and then keep adding the vals of the right pointer into the set
and keep track of result max length 
result would be right pointer - left pointer + 1, we can just use the index to get the lenght

'''



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in charSet:
                #want to remove from set from the left and update left pointer
                charSet.remove(s[L])
                L += 1
            #keep adding R vals to set
            charSet.add(s[R])
            res = max(res, R - L + 1)
        
        return res
                
