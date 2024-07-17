'''
we are given the head of a linked list, we have to figure out if there is a cycle
we know there is a cycle, if there is a node that is visited again from conitnsouly going next
there is no cycle, if we reach NULL
so we can have 2 pointers, slow and fast
both will start at the head
slow will be shifted by 1 
and fast will be shifted by 2

eventaully IF there is a cycle, fast and slow pointers will both meet indicating a cycle
and there is no cycle if fast ever reaches NULL

Time: O(n), of n input, on every iteration the distance between fast and slow is decreasing by 1
, so at n iterations, fast and slow will have met
Space: O(1)

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: #while fast is not NULL
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
