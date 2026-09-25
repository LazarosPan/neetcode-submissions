class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, n in enumerate(nums):
            if target - n in diffs:
                return [diffs[target - n], i]
            diffs[n] = i

        