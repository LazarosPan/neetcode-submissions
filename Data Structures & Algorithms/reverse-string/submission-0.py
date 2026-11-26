class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse s in-place using adjacent swaps.
        O(1) extra space, but O(n^2) time.
        """

        n = len(s)

        # Each pass moves one character toward its reversed position
        for i in range(n):
            current = n - 1

            # Move from the end toward the part already reversed
            while current > i:
                # Save the current character temporarily
                tmp = s[current]

                # Swap current with the character before it
                s[current] = s[current - 1]
                s[current - 1] = tmp

                # Continue moving toward the beginning
                current -= 1