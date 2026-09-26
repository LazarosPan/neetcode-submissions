from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # bucket[f] = numbers occurring exactly f times
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        # Highest frequencies first; stop as soon as we have k
        result = []
        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result