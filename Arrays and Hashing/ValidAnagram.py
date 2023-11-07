'''
Given 2 strings, s and t
Return True if t is an anagram of s
An anagram is a word formed by rearraning letters of a different word 
   - so that means original word, s, and rearranged word, t:
        - Must have:
                - Same length
                - Same characters 
                - the same occurence of each letter

So can start off with an initial check of the length
to check for same occruence of each letter use a hashmap
Create 2 hashmaps 
    one for s 
    one for t

    map letter to count of occurence 
    Compare hashmaps, if they are the same, return True they are anagrams 

Time Complexity: O(n) itearting through inputs once 
Space Complexity: O(n) for creating 2 hashmaps of size 

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for letter in s:
            if letter in sMap:
                sMap[letter] += 1
            else:
                sMap[letter] = 1
        for letter in t:
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1
        
        if sMap == tMap:
            return True
        return False
