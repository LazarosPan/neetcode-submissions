class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Return the minimum value in a rotated sorted array.

        Args:
            nums: A non-empty rotated array of unique integers.

        Returns:
            The minimum integer in nums.
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                # Minimum is at mid or to its left.
                right = mid
            else:
                # Mid cannot be the minimum.
                left = mid + 1

        return nums[left]