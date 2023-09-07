'''
we are given a string s and an integer k
the int k is the # of replacements we are allowed to make 
so we can start by having a count of occurences of a character in a window 

we will be using the sliding winod wtechnique to return the longest substring possible
how do we know if a substring is valid?
- if the length of the substring - the most frequent character is less than or equal to k
because if its more than k, that means we need more replacements that can be done, that would make the substring invalid
so we would have to move our left pointer

and since moving the left pointer, it would take out a character, so we would have to decrement the count of the char at the left pointer 
from the hashmap

we have to keep track of the result which is the size of the window 

and return result at the end


'''



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        L = 0

        for R in range(len(s)):
            # we need to add the character at R to the hashmap
            count[s[R]] = 1 + count.get(s[R], 0)

            if (R - L + 1) - max(count.values()) > k:
                #decrement L val from map
                count[s[L]] -= 1
                #shrink the size of the window
                L += 1
            
            #keep track of the window size
            res = max(res, R - L + 1)
            #continue updating R pointer
            R += 1
        return res


