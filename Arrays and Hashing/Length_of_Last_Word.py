'''
We are given a string s consisting of words and spaces
we have to return the length of the last word in the string

i could split the array by spaces
take the last index length and return that 
this solution would be a O(n) space complexity
O(n) time


'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitSpace = s.split(" ")
        # so theres the edge case where the last index is a space 
        # so i can create a loop to go through the array
        # if the char is a space, do nothing and go to the next
        # if its a word get the length
        for i in range(len(splitSpace)-1, -1, -1):
            if splitSpace[i] != "":
                return len(splitSpace[i])
        
