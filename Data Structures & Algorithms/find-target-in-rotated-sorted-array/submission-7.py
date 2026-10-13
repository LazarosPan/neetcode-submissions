class Solution:
    """Solution for searching a target in a rotated sorted array."""

    def search(self, nums: List[int], target: int) -> int:
        """
        Find the index of `target` in a rotated sorted array (unique values).

        Approach:
            Binary search over the index window [left_index, right_index].
            After computing the middle index, at least one of the two halves
            (left: left_index..middle_index, right: middle_index..right_index)
            is guaranteed to be sorted. Determine which half is sorted, check
            whether the target falls inside that sorted range, and discard the
            half that cannot contain the target.

        Args:
            nums: Unique integers sorted ascending, then rotated 1..n times.
            target: The value to look for.

        Returns:
            The index of `target` in `nums`, or -1 if it is not present.

        Complexity:
            Time:  O(log n), the search window is halved on every iteration.
            Space: O(1), only three index variables are used.
        """
        left_index = 0
        right_index = len(nums) - 1

        # Inclusive bounds: a single-element window must still be checked.
        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2

            if nums[middle_index] == target:
                return middle_index

            # Step 1: find a half whose endpoints can be trusted.
            # If nums[left] <= nums[middle], there is no rotation drop between
            # them, so the left half is sorted. "<=" (not "<") is required:
            # when left_index == middle_index the half is one element, which
            # is trivially sorted (e.g. [1, 3] -> left=0, middle=0).
            is_left_half_sorted = nums[left_index] <= nums[middle_index]

            if is_left_half_sorted:
                # Step 2: exact range test on the sorted left half.
                # Lower bound inclusive (nums[left] is unchecked); upper bound
                # exclusive (nums[middle] was already compared to target).
                is_target_in_left_half = (
                    nums[left_index] <= target < nums[middle_index]
                )
                if is_target_in_left_half:
                    # Target can only be here: drop the right half.
                    right_index = middle_index - 1
                else:
                    # Target is not in the sorted left half: drop it.
                    left_index = middle_index + 1
            else:
                # Left half contains the drop, so the right half is sorted
                # (values are unique, so there is only one drop).
                # Lower bound exclusive (middle already checked); upper bound
                # inclusive (nums[right] is unchecked).
                is_target_in_right_half = (
                    nums[middle_index] < target <= nums[right_index]
                )
                if is_target_in_right_half:
                    # Target can only be here: drop the left half.
                    left_index = middle_index + 1
                else:
                    # Target is not in the sorted right half: drop it.
                    right_index = middle_index - 1

        # Window exhausted without finding the target.
        return -1