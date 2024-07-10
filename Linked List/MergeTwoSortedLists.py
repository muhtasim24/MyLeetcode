
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
we have to merge 2 sorted lists into one
have to use the original nodes so we cannot make copies 
and in our output list, we dont know which of the first values of the lists is the min
so we can create a dummy node, and when returning the head we can just take the .next of our dummyNode
this elimates the edge case of inserting into an empty list

L1 : 1 -> 2 -> 4
L2 : 1 -> 3 -> 4 -> 5 -> 6
So while both lists are not empty, we can continue comparing each node, whichever is smaller
append to our output list
output: 1 -> 2 -> 3 -> 4, at this point we inserted all of L1 and nodes, 1 and from L2
L1 is not empty, and we still have 4, 5, 6 of L2
by the time we are here, in our algorithm we will be updating L1 and L2 as we append to our list
so we can continue moving foward
L2 will be at 4 -> 5 -> 6
l2 will be at the 4. so when l1 is empty, we can just append l2, as in, the rest of the list of l2

Time: O(n)
Space: Since we are creating the output list, O(n), size of the 2 inputs together

'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy #this is our head for now

        while list1 and list2:  #while list1 and list2 are not empty we can make comparisions
        #if l1.val is smaller than list2, append list1
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next #update pointer
            else: # else if the 2 values are equal to each other OR, list 2 is smaller
                tail.next = list2
                list2 = list2.next
            tail = tail.next # need to update our tail pointer as well everytime
        
        #now if list1 is NOT empty and list2 IS, just append to the rest of list1
        if list1:
            tail.next = list1
        # if list2 is NOT empty and list1 IS, just append the pointer of where list2 currently is
        # we are just appending the list itself, and the rest of the elemens will come with
        elif list2:
            tail.next = list2

        return dummy.next
