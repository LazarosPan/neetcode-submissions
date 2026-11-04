class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort an array containing only 0s, 1s, and 2s in-place.

        Uses the Dutch National Flag algorithm with three pointers:
        - left: position where the next 0 should be placed.
        - current: position currently being inspected.
        - right: position where the next 2 should be placed.

        During the algorithm:
        - Everything before `left` is 0.
        - Everything after `right` is 2.
        - Elements between `current` and `right` are not yet processed.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        left = 0  # next position where a 0 should go
        current = 0  # index of the number we are checking
        right = len(nums) - 1  # next position where a 2 should go

        while current <= right:  # continue while there are unchecked numbers
            if nums[current] == 0:
                temp = nums[left]  # temporarily store the left value
                nums[left] = nums[current]  # move the 0 to the left
                nums[current] = temp  # move the stored value to current
                left += 1  # next 0 goes one position further right
                current += 1  # continue with the next number

            elif nums[current] == 2:
                temp = nums[right]  # temporarily store the right value
                nums[right] = nums[current]  # move the 2 to the right
                nums[current] = temp  # move the stored value to current
                right -= 1  # next 2 goes one position further left
                # Do not move current because the swapped value is unchecked.

            else:
                current += 1  # 1 is already in the correct region