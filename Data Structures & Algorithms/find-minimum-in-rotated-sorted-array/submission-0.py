class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        nums.sort()
        return nums[0]