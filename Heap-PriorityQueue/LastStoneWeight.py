'''
so we are given an array of integers stone, where stones[i] is the weight of the ith stone
on each turn we are smashing the heaviest stones together
lets say stones have weight x and y, where x <= y
If x == y, they are both destoryed
if x !=, that means x is smaller than y, x is destoryed, y has a new weight of y - x
and new y is added back to the stones weight

so we can use a minHeap, maxHeap doesnt exist
so how we would do that, is turn all the weights of the stones into negative 
so when we try to retrieve the min, take the absolute value, and that value will actaully be the heaviest stone

so first take stones
iterate through, turn all values negative
heapify it so its a minHeap now

then we can iterate through the minHeap, till we are left with 1 stone, or none


'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        print(stones) # stones are now all negative 

        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) # first largest
            x = heapq.heappop(stones) # second largest, so x <= y

            # since already popped if weights are the same dont do anything
            if abs(x) < abs(y):
                y = (abs(y) - abs(x)) #new weight, add back into heap
                heapq.heappush(stones, y * -1)
            
        if stones:
            return abs(stones[0])
        else:
            return 0




        
