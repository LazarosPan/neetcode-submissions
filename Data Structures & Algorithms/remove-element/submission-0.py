class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        # k is the index where we will place the next valid element
        k = 0

        # i scans every index in the original array
        for i in range(len(nums)):
            # Keep the current element only if it is not equal to val
            if nums[i] != val:
                # Move the valid element to the next available position
                nums[k] = nums[i]

                # Advance k because we added one valid element
                k += 1

        # k is also the number of elements that are not equal to val
        return k