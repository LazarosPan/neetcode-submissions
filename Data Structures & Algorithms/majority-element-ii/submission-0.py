class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Finds all values that appear more than floor(len(nums) / 3) times.

        At most two such values can exist: three of them would need more than
        len(nums) elements in total. Two candidate slots are therefore enough.

        The algorithm has two phases:
        1. Candidate selection. Track two candidates with one counter each.
            When a value matches neither candidate and both counters are in use,
            decrement both. This discards threealues at once, which
            can never fully eliminate a value occurring more than n/3 times.
        2. Verification. The survivors are only candidates (for example, [1, 2,
            3] leaves two of them), so their true frequencies are counted.

        Time complexity: O(n). One pass selects candidates, one pass verifies.
        Space complexity: O(1). Four counters/candidates, output of at most 2.

        Args:
        nums: The input integers.

        Returns:
        The values occurring more than floor(len(nums) / 3) times, in any order.
        """
        first_candidate: Optional[int] = None  # At most 2 answers exist.
        second_candidate: Optional[int] = None
        first_votes = 0  # Net count after cancellations.
        second_votes = 0

        # Phase 1: select up to two candidates.
        for num in nums:
            if num == first_candidate:  # Tracked values are matched first.
                first_votes += 1
            elif num == second_candidate:
                second_votes += 1
            elif first_votes == 0:  # Free slot: adopt the new value.
                first_candidate = num
                first_votes = 1
            elif second_votes == 0:  # Free slot: adopt the new value.
                second_candidate = num
                second_votes = 1
            else:
                first_votes -= 1  # Discard three distinct values together:
                second_votes -= 1  # num and one copy of each candidate.

        # Phase 2: candidates are only possible answers, so count them exactly.
        first_occurrences = 0
        second_occurrences = 0
        for num in nums:
            if num == first_candidate:
                first_occurrences += 1
            elif num == second_candidate:
                second_occurrences += 1

        min_occurrences_exclusive = len(nums) // 3  # Must appear MORE than this.
        result = []
        if first_occurrences > min_occurrences_exclusive:
            result.append(first_candidate)
        if second_occurrences > min_occurrences_exclusive:
            result.append(second_candidate)
        return result
            
