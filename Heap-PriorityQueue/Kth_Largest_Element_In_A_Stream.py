'''
we are given a integar array nums and int k
we have to design the class to be able to take a stream of numbers
and also be able to add to that stream

we have to return the kth largest value in the stream everytime we add a number
so how can we do this
Using a minHeap

To be exact, using a minHeap of Size K 
so if k = 3
and our minHeap is the lenght of 3, we want to return the 3rd largest
getting the minimum value from a minHeap, takes O(1) time
heap have sorting property so min is already at the 0th index

lets say we have 4,5,8,2 to begin with k = 3
and we turn that array into a heap
so now its sorted
[2, 4, 5, 8] length(4) > k(3), so we need to pop from the heap till we have size k
[4, 5, 8]

now we have a minHeap of size k
so when we return the kth largest, it will actually be the minimum of the heap

when we add a value to the stream, we are going to add no matter what
but we will only pop from the heap IF adding cause our length of the heap to be larger than k



'''



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) #turns array into heap

        while len(self.minHeap) > k: # turn the heap into size k, by popping till we have length == k
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #push the val to the heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # pop min val if we went over size k for minHeap

        return self.minHeap[0] # return the min value to get the kth Largest 
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
