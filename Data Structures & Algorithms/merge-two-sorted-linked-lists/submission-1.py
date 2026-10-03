# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # both l1 and l2 are sorted
        # return the head of the new single sorted linked list
        # in case one list is empty just return the other
        # if both empty, return empty list
        # can be solved in O(n+m) time and O(1) space, n = len(list1), m = len(list2)
        # we should avoid creating a new list to consume less space

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
            
        # One list may still contain nodes.
        # Attach its entire remaining chain.
        tail.next = list1 if list1 else list2
        
        return dummy.next