'''
Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all original letters exactly once


'''





class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #mapping charCount to list of Anagrams 

        for s in strs: 
            count = [0] * 26   # initlizes an array of 26 indices with all 0s -> a...z

            for chars in s: 
                count[ord(chars) - ord("a")] += 1 #maps the ascii values to the correct index
                                                # a = 80 - 80 = 0
                                                # b = 81 - 80 = 1
                                                # c = 82 - 80 = 2
            #now we created the list keys, for example 1e, 1a, 1t
            # now we need to add the strings that follow the list keys 

            result[tuple(count)].append(s)   # this will append any strings that have the charCoutns 

        # we only want the list of strings not the charCounts as well, so only return the values

        return result.values()

#time complexity is O(m * n * 26) -> O(m * n)
# m is the size of the input
# n is the avg size of the strings in the input array



