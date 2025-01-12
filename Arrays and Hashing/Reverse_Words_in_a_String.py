'''
we are given an input string s, we need to reverse the order of the words
the words in s are spearated by AT LEAST one space, meaning there could be more
but in our reversed string we do not want multiple spaces between words OR 
trailing or leading spaces

so we could we use 2 pointers, one at the beginning and one at the end 
and just keep swapping characters

   pointers approach, spit the string
and keep swapping the words[left] = words[right]
we will need a temp variable
then at the end, we can just the array words, into one string with a space delimiter


'''



class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() #split the words, takes away spaces from the strings
        left, right = 0, len(words) - 1

        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left+= 1
            right -= 1
        
        return ' '.join(words)

'''
REVERSE ITERATION METHOD ------------------------------------------------------------------------------------------
we are given an input string s, we need to reverse the order of the words
the words in s are spearated by AT LEAST one space, meaning there could be more
but in our reversed string we do not want multiple spaces between words OR 
trailing or leading spaces

so we could we use 2 pointers, one at the beginning and one at the end 
and just keep swapping characters

lets handle the case of first finding the start points, as in the first word
we will have while loops for our pointers, 
while the pointers == space, we will keep updating them
now we have the start 

but we cant have spaces in our return leading or trailing 
soo create a new string, or maybe we can use a pointer to mark the end of the string
yes
so start and end same procedure
and we also have to keep track of the last character too, since we dont want mulitple spaces
in between words

understood the problem wrong 
we are swapping the words itself
reversing words order
not reversing the string

so we could split the array
we will have all the words and no spaces included
we will iterate through this array in revers eorder
we need a space in between every string, so we can include one after everytime we append to our newStr

the ONLY time we dont need to add a space is when we are the beginning of the array, as in the 0th index
since we would be at the end of the reversed order
SO, in that case we just append that index string without a space included


'''



class Solution:
    def reverseWords(self, s: str) -> str:
        spaceSplit = s.split()
        print(spaceSplit)

        newStr = ""
        for i in range(len(spaceSplit)-1, -1, -1):
            if i == 0:
                newStr += spaceSplit[i]
            else:
                newStr += (spaceSplit[i] + ' ')
        return newStr

    
