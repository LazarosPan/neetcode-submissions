class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]  # Initial candidate; nums is guaranteed nonempty
        balance = 0         # Uncancelled votes, not the actual frequency

        for num in nums:
            if balance == 0:
                candidate = num  # No votes remain; start with this number

            if num == candidate:
                balance += 1  # Matching number adds a vote
            else:
                balance -= 1  # Different number cancels one candidate vote

        return candidate  # Guaranteed majority survives pair cancellation

# Boyer–Moore majority vote algorithm.
# Initialize an element m
# Initialize a counter c ← 0
# for each element x of the input sequence:
#     if c = 0, do 
#         m ← x
#         c ← 1
#     else if m = x, do
#         c ← c + 1
#     else do
#         c ← c - 1
# return m