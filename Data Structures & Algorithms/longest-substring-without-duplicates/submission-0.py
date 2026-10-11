class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}      # char -> last index where it was seen (not "window contents")
        left = 0       # window is s[left..right], always duplicate-free
        best = 0

        for right, char in enumerate(s):   # right = index of the char being processed
            # Duplicate inside the window only if seen before AND its index >= left.
            # If last[char] < left, the entry is stale (outside the window): ignore it.
            if char in last and last[char] >= left:
                left = last[char] + 1      # jump just past the previous occurrence

            last[char] = right             # always record the latest index
            best = max(best, right - left + 1)

        return best                     # "" -> 0, "bbbbb" -> 1, no special cases