import random
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > majority_count:
                return candidate