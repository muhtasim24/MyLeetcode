'''
We are given 2 strings s and t,
we have to return true if s is a subsequence of t or false otherwise

so bascially all of s has to be in t for it to be a subsequence 
and the characters must show up in the order of s
ex:
s="ace" is a subsequnce of "abcde"
                            - - -
but aec is not of "abcde" since c comes before e
so im thinking we could have 2 pointers 
one at s and one at t 
once the pointer of t equals the pointer of, we could move s pointer
if we reach the end of t wihtout returning true that means we have no subsequnce


'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPoint = 0
        tPoint = 0

        # edge case where t is larger than s, s cant be a subsequence if t is smaller
        if len(t) < len(s):
            return False

        # if s is empty, then its always a subsequnce of t
        if s == "":
            return True
        
        # make sure we are always within bounds
        while tPoint < len(t):
            if s[sPoint] == t[tPoint]:
                sPoint += 1
                if sPoint >= len(s):
                    return True
            # always updating tPoint
            tPoint += 1
        return False
