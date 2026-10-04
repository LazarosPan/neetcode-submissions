# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # we can use fast and slow pointers, Floyd's Tortoise and Hare algorithm
        # cycle: at least one node can be visited again by .next
        # if index == -1 then tail -> null, no cycle
        # if index != -1 then cycle
        # keep a dict of the nodes visited

        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True
        
        return False