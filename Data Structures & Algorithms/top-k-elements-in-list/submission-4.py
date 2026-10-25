from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Return the k most frequent distinct values in any order.

        Args:
            nums: A nonempty list of integers.
            k: Number of values to return, between 1 and the number
                of distinct values in nums.

        Returns:
            A list containing the k most frequent values.
            The selection is guaranteed to be unique.

        Complexity:
            O(n) expected time and O(n) space, where n = len(nums).
        """
        # Count how many times each value appears.
        frequencies = Counter(nums)

        # A value can appear at most len(nums) times.
        maximum_frequency = len(nums)

        # buckets[frequency] will hold values occurring that many times.
        buckets = []
        for frequency in range(maximum_frequency + 1):
            buckets.append([])

        # Store each distinct value in the bucket matching its frequency.
        for value, frequency in frequencies.items():
            buckets[frequency].append(value)

        # Reverse the buckets to process the highest frequencies first.
        buckets.reverse()
        result = []

        # Buckets have already been reversed: highest frequency first.
        for values in buckets:
            result.extend(values)

            # Keep exactly k values once enough have been collected.
            if len(result) >= k:
                return result[:k]
        
        # # OR
        # # Each bucket can contain multiple values with the same frequency.
        # for values in buckets:
        #     for value in values:
        #         result.append(value)

        #         # Stop once exactly k values have been collected.
        #         if len(result) == k:
        #             return result