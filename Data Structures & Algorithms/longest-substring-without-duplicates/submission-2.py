from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        counts = defaultdict(int)
        left = 0
        best = 0

        for right, char in enumerate(s):
            counts[char] += 1
            
            while counts[char] > 1:
                counts[s[left]] -= 1
                left += 1
            window = right-left+1
            best = max(best, window)
        return best