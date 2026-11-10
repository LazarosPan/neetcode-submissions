from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the smallest positive integer that is missing from `nums`.

        Approach: cyclic sort (in-place index hashing).
        The answer always lies in [1, n + 1], where n = len(nums), so only
        values in 1..n matter. Each such value `v` is moved to index `v - 1`.
        After placement, the first index holding the wrong value reveals
        the missing number.

        Args:
            nums: Unsorted list of integers (may contain negatives,
                  zeros and duplicates). It is modified in place.

        Returns:
            The smallest positive integer not present in `nums`.

        Complexity:
            Time:  O(n), because every swap puts one value in its final slot.
            Space: O(1), because the input array is reused.
        """
        array_length = len(nums)

        # Phase 1: place each value v (1 <= v <= n) at index v - 1
        for current_index in range(array_length):
            # Keep swapping until the value at current_index is either
            # out of range or already sitting in its correct slot
            while (
                1 <= nums[current_index] <= array_length
                and nums[nums[current_index] - 1] != nums[current_index]
            ):
                # Index where the current value belongs
                target_index = nums[current_index] - 1

                # Swap the current value into its correct position
                nums[current_index], nums[target_index] = (
                    nums[target_index],
                    nums[current_index],
                )

        # Phase 2: the first slot that doesn't hold (index + 1) is the answer
        for position in range(array_length):
            expected_value = position + 1
            if nums[position] != expected_value:
                return expected_value

        # All of 1..n are present, so the next positive integer is missing
        return array_length + 1