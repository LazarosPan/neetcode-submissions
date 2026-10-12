from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Returns the longest substring of one repeated character.

        Args:
            s: Input text, consisting of uppercase English letters.
            k: Maximum number of characters allowed to be replaced.

        Returns:
            The length of the longest substring that can be made of a single
            repeated character using at most k replacements.
        """
        # Character counts inside the window; unseen characters start at 0.
        char_count = defaultdict(int)
        left = 0
        longest_length = 0

        for right, char in enumerate(s):
            # Grow the window first, then repair it if it became invalid.
            char_count[char] += 1

            # window length = right - left + 1
            # max frequency = count of the most common character in the window
            # Replacements needed = window length - max frequency, because we
            # keep the most common character and replace the rest.
            # Removing one character may not be enough, hence the while loop.
            while (right - left + 1) - max(char_count.values()) > k:
                # Keep counts in sync with the window.
                char_count[s[left]] -= 1
                left += 1

            # The window is valid here, so it is a candidate answer.
            longest_length = max(longest_length, right - left + 1)

        return longest_length