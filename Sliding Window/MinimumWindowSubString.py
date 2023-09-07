'''
the string s needs to have the ALL the characters from string t
we need to find the minimum substring window that has the all the chars from t 
we can have 2 hashmaps 
1 hashmap to keep track of the characters we care about, as in the chars in t that are in the window 

1 hashmap to keep track of the count of each character in t

we can initlize the countT map first 

so we are going to be using the sliding window technique 

everytime we increase our window size, or move the right pointer 
we are going to add the character with a count to the window map IF and ONLY IF, that same character is in t

the countT map will give us the length of characters we need and we will have another variable have
have must equal to need for it to be a valid substring 

but we want the min
so when we have a valid substring, we can keep track of the length of that window 
and then decrement from the left pointer, and remove that character from the window count if it was in T

we only care for characters in T that are in S


'''



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if t == "":
            return ""
        
        #initlize the 2 maps
        countT, window = {} , {}

        #initlize countT map because that will never change 
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        #the variabels have and need 
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        L = 0

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0) #increment window map

            #since we only care about the charactrers of T in S
            #if the char we just got to, is a char in T, and the counts are the same from both hashmaps 
            #for ex, we need 1 B and in our window we just added 1 B, that means we have a value that we need 
            # so increment have
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #update our result
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = (R - L + 1)
                
                #pop from the left of our window, so we can continue trying to find a min length
                window[s[L]] -= 1

                #and then when we pop from the left, if the char we popped was in T and now the count of that char in window is less than 
                #the count we need of a specific char, we would need to decrement have 
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                #keep moving left pointer
                L += 1
        
        L, R = res

        return s[L:R + 1] if resLen != float("infinity") else ""
