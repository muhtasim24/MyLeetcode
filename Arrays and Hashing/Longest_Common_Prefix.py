'''
we are given an array of strings
we need to find the longest common prefix 
which is basically from the beginning of every string
what continous characters do all strings share

so ex:
strs = ["flower","flow","flight"]
we see 
all 3 strings share fl
so output = fl

so how would we find this common prefix
we will simulatenously go through every index of every string
and we're not going to compare every single string to every other single string

we can just choose one string and compare it to every other string
because THEY ALL need to have the common prefix, so if the one we choose doesnt, then no common prefix
or lets say we get out of bounds when comparing strings
if a string we are at is smaller than the index we are at, we can stop the algo
since there will be no more common prefix with that string, and We need the common prefix for ALL

ex:
strs = ["flower","flow","flight"]
         _        _      _
         they all have f, lets say we'll compare every string to the first string
         and iterate through the index
         we will keep going as they are equal, once they are not we can return our result

strs = ["flower","flow"]
         ____     ____
        we see both these strings have a common prefix of flow, but when we go to compare the 
        e from flower, there is not 5th index for flow, so if the index we are at is out of bounds
        for any of the strings, we need to stop the algo

        and notice how these 2 stirngs have flow, but flight does not
        so common prefix is just "fl"

Time Complexity: O(n * m) , n = avg size of strings , m = # of strings in array


'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # we will just choose to go through the indexes of the first string,
        # doesnt really matter whcih string we go through for the index
        # they ALL need to havethe same prefix
        for i in range(len(strs[0])):
            # then we will go through every string in the array
            for s in strs:
                #make sure the index we are at is not out of bounds for any string
                # and again just comparing the first string to every other string
                # if string[i] != first string[i] then not a common prefix, dont add
                # we are going through every single string continously 
                if i > len(s)-1 or s[i] != strs[0][i]:
                    return res
                # once we go through every single string for that index
                # we can add the value at the index of the first string to our res
                # since all strins share the same character at the same index
                # so a common prefix
            res += s[i]
        return res
