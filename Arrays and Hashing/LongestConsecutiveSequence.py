'''
Understand: 
Can visualize the array into blocks 
Ex: [100,4,200,1,3,2]
The block we need is 1,2,3,4 because that is the consecutive sequence 

Match:
Use a Set 

Plan: 
Make a set out of the array to check if a element is in there or not, so no dups 
initlize a longest variblale to hold the count of the largest 

loop over the array 
find the starting sequence 
for n in set 
    if n - 1 is not in set: (to check if its beginning of sequency)
    length = 0 
    while(n + length), use length to update to keep adding to sequence 
    length += 1
    update length. 1+1 = 2 
    now if 2 is in set, we increment length of sequenc, now if 2 + 1 = 3, is in set, we increment. same thing while happen for 4, and then we set longest to the max (length, longest)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of the sequence 
            # if n-1 not in Numset then it IS a start of a sequence 
            
            if (n - 1) not in numSet:
                length = 0
                # check if 
                while (n + length) in numSet: 
                    #update length because we found a consequtive number after our starting 
                    #so 1+1 = 2, if found 2, keep oging, increment length, 1+2 = 3, if found 3, keep going,
                    # increment length 1 + 3, if found 4, keep going. increment length. 1 + 4. 5 is not in the set, so we have length = 4, and then do max(length, longest). and longest will give us either the previous largest sequence, or if length is larger than longest, return us value of length, and set to longest
                    length += 1
                    # update longest, from previous sequence in case that was a sequnce. 
                    # max will give us max between current length, and previous largest sequence 
                longest = max(length, longest)
        return longest
                
