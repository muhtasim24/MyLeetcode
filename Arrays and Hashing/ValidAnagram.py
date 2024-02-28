'''
we are given 2 strings
return True if t is an anagram of s, false otherwise

anagram = a word or phrase formed by rearranging the letters of a different word 
so that means 
if they are anagrams, the following is true:
    - same length
    - each character shows up the same number of times in both s and t
if either of that is False, not an anagram

to keep track # of times a character shows up in s and t
we can have 2 maps
and once the map is filled, letter -> count
the maps should be the same


'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        if len(s) != len(t):
            return False
        
        for i in s: 
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1

        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1

        return tMap == sMap
            
        

        
