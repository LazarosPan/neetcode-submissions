class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # edge case
        if not nums:
            return 0

        # O(1) lookups and remove duplicates
        num_set = set(nums)

        # longest sequence found so far
        longest_streak = 0

        for num in num_set:

            # only start counting from the beginning of a sequence
            # e.g. start at 2, skip 3,4,5 because their predecessor exists
            if num - 1 not in num_set:

                current_num = num
                current_streak = 1

                # count forward: 2->3->4->5...
                # we can do this because the set already contains all numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # keep the longest sequence length seen
                longest_streak = max(longest_streak, current_streak)

        return longest_streak