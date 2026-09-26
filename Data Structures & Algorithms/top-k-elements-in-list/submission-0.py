from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        # bucket[i] contains numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result