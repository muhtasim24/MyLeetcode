'''
So we are given 2 strings, needle and haystack
we have to return the index of the first occurence of needle in haystack
if needle is NOT a part of haystack return -1

ex:
haystack = "sadbutsad", needle="sad"
so we have to find out if needle,"sad", exists within the haystack's string, sadbutsad,
we see that it does but what we have to return is the first occurence
so the very first sting in haystack that is the start of the string from needle

another ex:
haystack: "leetcode"  needle = "leeto"
we have to find out if leeto exists within leetcode 
we see leeto DOES NOT exist, 

so my approach
get the length of needle string
have 2 pointers that will start at the index of the beginning of needle
and a pointer that will start at the end of needle

with that range, we will have a substring to check everytime within haystck
so we will go through haystack, checking that range, and keep updating the pointers 1 by 1
might be very slow


'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        left = 0
        right = len(needle) - 1

        while right < len(haystack):
            if haystack[left:right+1] == needle:
                return left
            else:
                left += 1
                right += 1

        return -1
