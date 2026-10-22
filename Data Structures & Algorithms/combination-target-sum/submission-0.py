class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Return all unique combinations of `nums` that sum to `target`.
        Each number may be reused any number of times.

        Approach: backtracking (DFS over an implicit decision tree).
        Choosing only from `start_index` onward prevents the same
        combination appearing in a different order, e.g. [2,5] and [5,2].

        Time:  O(2^(t/m)), t = target, m = min(nums)
        Space: O(t/m), the maximum recursion depth
        """
        valid_combinations = []
        current_combination = []  # numbers chosen on the current path

        def backtrack(start_index: int, remaining_target: int) -> None:
            # Base case: the current combination sums exactly to target
            if remaining_target == 0:
                # Snapshot it, because current_combination keeps changing
                valid_combinations.append(current_combination.copy())
                return

            for candidate_index in range(start_index, len(nums)):
                candidate = nums[candidate_index]

                # Prune: this number overshoots the remaining target
                if candidate > remaining_target:
                    continue

                current_combination.append(candidate)  # choose
                # Pass candidate_index (not +1) so the same number can be reused
                backtrack(candidate_index, remaining_target - candidate)
                current_combination.pop()              # undo choice (backtrack)

        backtrack(0, target)
        return valid_combinations