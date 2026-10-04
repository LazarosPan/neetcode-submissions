class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting enables two-pointer search and groups duplicates together.
        nums.sort()

        result = []

        # Fix nums[i] as the first value of each triplet.
        # Stop at n - 2 because two values must remain after i.
        for i in range(len(nums) - 2):

            # Reusing the same fixed value would produce duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Search for two values whose sum equals -nums[i].
            left = i + 1
            right = len(nums) - 1

            # left < right ensures all three indices are distinct.
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # The sum is too small.
                    # Move left rightward to select a larger value.
                    left += 1

                elif total > 0:
                    # The sum is too large.
                    # Move right leftward to select a smaller value.
                    right -= 1

                else:
                    # A valid unique triplet was found.
                    result.append([nums[i], nums[left], nums[right]])

                    # Continue searching for other triplets using nums[i].
                    left += 1
                    right -= 1

                    # Skip left values already used in the previous triplet.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip right values already used in the previous triplet.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result