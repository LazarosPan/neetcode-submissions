# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder a singly linked list in place:
            L0 -> L1 -> ... -> Ln-1   becomes   L0 -> Ln-1 -> L1 -> Ln-2 -> ...

        Approach (3 phases):
            1. Find the middle with slow/fast pointers.
            2. Reverse the second half.
            3. Interleave the first half and the reversed second half.

        Time:  O(n)  - each phase is a single linear pass.
        Space: O(1)  - only a constant number of pointers; nodes are relinked,
                       never copied, and values are never modified.
        """
        # Lists of length 0 or 1 are already in the required order.
        if not head or not head.next:
            return

        # ---- Phase 1: find the middle ----
        # fast moves 2x as fast as slow, so when fast hits the end,
        # slow sits at the end of the first half.
        # For n=5 [0,1,2,3,4\]: slow ends on 2. For n=4 [0,1,2,3\]: slow ends on 1.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Detach the halves. The second half starts right after slow.
        # First half is therefore >= second half in length (odd n: middle stays in first).
        second = slow.next
        slow.next = None  # terminate first half so it doesn't loop back into second

        # ---- Phase 2: reverse the second half in place ----
        # Standard iterative reversal: flip each node's next pointer.
        prev = None
        while second:
            nxt = second.next   # save the rest of the list before overwriting
            second.next = prev  # flip pointer backwards
            prev = second       # advance prev
            second = nxt        # advance current
        second = prev           # prev is now the head of the reversed half

        # ---- Phase 3: interleave the two halves ----
        # Take one node from the first list, then one from the second, repeat.
        first = head
        while second:           # second is the shorter (or equal) list, so it ends first
            first_next = first.next    # save both successors BEFORE relinking
            second_next = second.next

            first.next = second        # L0 -> Ln-1
            second.next = first_next   # Ln-1 -> L1

            first = first_next         # move on in both lists
            second = second_next
        # Leftover first-half node (odd n) is already linked correctly: its next is None.