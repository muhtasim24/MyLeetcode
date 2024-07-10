'''
we are given an array of int temperatures
we have to return an output array answer, where each index 
is the number of days it took to find a higher temperature 
If no temperature is found that is higher, index can have 0

so we can have a monotomic decreasing stack
We append to the stack every temperature, and when we find an element that is higher 
than the temperature at top of the stack, pop from the stack
and put in the days it took, how do we keep track of the days it took
we can actually put in a pair of values in the stack
we will append the temperature, and the index of that temperature
we will append the difference of the higher temp, and temp from the top of the stack to output array

ex:
input: [73,74,75,71,69,72,76,73]
stack: 73, 74
we found 74, is higher than 73, no need to remember 73 anymore so pop it
add 1 to output
stack: 74, 75
same thing
stack: 75, 71, 69
71 and 69 are not larger than 75, so we cannot pop
stack: 75, 71, 69, 72
72 is larger than 69, so pop that. and its also larger than 71, so that can be popped
stack: 75, 72, 76
put difference of index in output array after popping
stack: 76, 73
73 is end of list and no temp is higher than 76 or 73 in future days, since its the end 
so already initalied to 0

Time: O(n) for iterating through the input 
Space: O(n) for the stack

'''



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we will append pairs, the tempearutre and index of that temperature

        for index, temp in enumerate(temperatures):
            #while stack is not empty and new temp is larger than top of stack
            while stack and temp > stack[-1][0]: #need to add index 0 after cause our stack has pairs
            #and the top of the stack index is the first element so it is always 0th index
                #so while this is true, continue popping 
                stackTemp, stackIndex = stack.pop()
                #append the difference of index to the output list in the correct index
                res[stackIndex] = (index - stackIndex)
            #push the new temperature and its index to the stack
            stack.append([temp, index])
        return res
