from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        print(counter)
        reverse = {v: k for k, v in counter.items()}  # O(n), once
        return reverse.get(max(counter.values()))