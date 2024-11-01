'''
are so we are given an integer array nums and integer k, we have to return the kth largest element in the array
this is kth largest in the sorted order, not kth distinct 

so we can use a maxHeap for this, which is really a minHeap with negative values
we turn all the values in nums negative
heapify nums, so its all sorted

Now the largest elements will be our min
and im assuming we are never adding new values so this can work
We can have a count of number times we've popped
when that number == k, we can return the last number we just popped

a simpler solution would just turn into heap, and keep popping till len(heap) < k
so while len(heap) > k:
keep popping
Once len(heap) == k:
we can just return the min of that size of heap
that means it would be the kth Largest
if k = 3
[1, 2, 3, 4, 5, 6]
we would have popped 1,2,3
and now heap = [4, 5, 6]
and kth largest, 3rd largest, would be the min of the new heap, which is 4

'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        # after while loop we should have a heap of size k
        # the min would be the kth Largest element
        return nums[0]
        

