class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse s in-place using O(1) extra memory.
        """

        left = 0               # Start of the string
        right = len(s) - 1     # End of the string

        # Continue until the two pointers meet/cross
        while left < right:
            # Swap the characters at both ends
            s[left], s[right] = s[right], s[left]

            # Move both pointers toward the center
            left += 1
            right -= 1