class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}   # char -> how many times it appears in the current window
        left = 0      # window is s[left..right]
        best = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1   # 1. add s[right] to the window

            while counts[char] > 1:                  # 2. window invalid: char is duplicated
                counts[s[left]] -= 1                 #    remove the leftmost char
                left += 1                            #    shrink from the left

            best = max(best, right - left + 1)       # 3. window is valid again: record length

        return best                                  # "" -> 0, "bbbbb" -> 1