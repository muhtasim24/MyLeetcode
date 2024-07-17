'''
we are given a list
we have to reorder it, by following: L0 -> Ln -> L1 -> Ln-1
first, last, second, 2nd to last, third
basically 2 lists, but going from the start of the first half and end of the 2nd half
so since we are starting at the 2nd half of the list
we can actually reverse that list so we can use the .next properly 

how do we reverse the 2nd half of the list
we need to find the start of it
we can have 2 pointers, slow and fast
slow starts at head, fast starts at head.next
slow moves by 1, fast moves by 2
by the time fast reaches the end of the list,
slow will be at the end of the first list, so slow.next will be the start of the 2nd list

we can reverse the list,
saving links in temp varaibles
applying the changes in place

now after reversing the list,
we have to merge 
Since we are doing it in place, we need to save the links of the first.next and second.next
first is the first list, second is the start of the 2nd list
first -> second -> first.next -> second.next 

[1, 2].  [4, 3]
 F  f1    S  s1
save the .next of F and S
F -> S -> f1
the update our pointers
F goes to f1
and Second goes to s1, second .next
dont need to return, this will merge and reorder the lists
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find the second half of the list
        slow, fast = head, head.next
        #till we reach the end with fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #start of 2nd list is the .next of where the slow pointer is
        second = slow.next
        #reverse the 2nd list
        # make the previous None
        prev = slow.next = None
        while second:
            tmp = second.next #save the original .next
            second.next = prev #update the .next of second to reverse it
            #update pointers
            prev = second
            second = tmp
        
        #now merge the lists
        # prev is the head of the 2nd list (reversed)
        # head is the head of the 1st list
        first, second = head, prev
        # the 2nd list more liekly to be a shorter list so while second list is not empty
        while second: 
            #save the links before updating 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1
