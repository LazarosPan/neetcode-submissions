class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_count = len(nums)
        set_count = len(set(nums))
        if list_count != set_count:
            return True
        else: return False