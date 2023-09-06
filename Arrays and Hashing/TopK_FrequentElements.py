'''
Understand: 
I am given a array, nums, and a int, k
k is most frequent element 
is there letters, or special characters
Find the elements that match the k frequency
Is there an emp

Match:
Hashmap

Plan: 
Initlize a hashmap 
I want to map the keys, which is the elements in the array, to a value, count/frequency 
Loop over array 
If key is in array, increment value by 1 
if key is not in array, add key to array and assign it value 1

Now I have hashmap 

Loop over hashmap

If values match int k, 
add key or hashmap[i] to list
return list




'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        listy = []
        dictt = {}
        
        for i in nums: 
            if i in dictt: 
                dictt[i] += 1
            else:
                dictt[i] = 1
        
        for i in dictt: 
            for j in dictt:
                if dictt[i] > dictt[j]:
                    listy.append[i]
        
        return listy
                
                
                
                
                
                
                
                
                
