from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Find the total number of contiguous, non-empty subarrays
        whose sum equals k.

        Approach:
            Use prefix sums and a hash map to count how many
            previous prefix sums can form a subarray summing to k.

            Mathematical observation:
                subarray_sum = current_prefix_sum - previous_prefix_sum

                We want:
                    current_prefix_sum - previous_prefix_sum = k

                Therefore:
                    previous_prefix_sum = current_prefix_sum - k

            For each element:
                1. Update the running prefix sum.
                2. Count previous prefix sums equal to (prefix_sum - k).
                3. Record the current prefix sum in the hash map.

        Args:
            nums: Array of integers (-1000 <= nums[i] <= 1000).
            k: Target sum (-10^7 <= k <= 10^7).

        Returns:
            Number of contiguous subarrays whose sum equals k.

        Constraints:
            1 <= len(nums) <= 20_000

        Complexity:
            Time: O(n) - Single traversal of nums.
            Space: O(n) - Hash map storing prefix sum frequencies.
        """

        # Key: prefix sum
        # Value: frequency of that prefix sum
        prefix_counts = defaultdict(int)

        # Represents the empty prefix before index 0
        prefix_counts[0] = 1

        prefix_sum = 0
        count = 0

        for num in nums:
            # Update cumulative sum
            prefix_sum += num

            # Count previous prefix sums that produce target k
            required_sum = prefix_sum - k
            count += prefix_counts[required_sum]

            # Record current prefix sum
            prefix_counts[prefix_sum] += 1

        return count