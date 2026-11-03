class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        total_elements = len(nums)
        
        # Base case: An empty array or single element is already sorted
        if total_elements <= 1:
            return nums

        # The size of the small sub-chunks we want to sort using Insertion Sort first.
        # Real Timsort dynamically calculates this between 32 and 64, but 32 works here.
        TARGET_RUN_SIZE = 32

        # ---------------------------------------------------------------------
        # PHASE 1: BINARY INSERTION SORT SUBROUTINE
        # ---------------------------------------------------------------------
        def binary_insertion_sort(start_index: int, end_index: int):
            """Sorts a small segment of the array in-place."""
            for current_target_index in range(start_index + 1, end_index + 1):
                value_to_insert = nums[current_target_index]
                
                # Perform a binary search to find exactly where this value belongs
                search_left_boundary = start_index
                search_right_boundary = current_target_index - 1
                
                while search_left_boundary <= search_right_boundary:
                    midpoint_index = (search_left_boundary + search_right_boundary) // 2
                    if nums[midpoint_index] > value_to_insert:
                        search_right_boundary = midpoint_index - 1
                    else:
                        search_left_boundary = midpoint_index + 1
                
                # Shift all larger elements one position to the right to clear a spot
                for shift_index in range(current_target_index - 1, search_left_boundary - 1, -1):
                    nums[shift_index + 1] = nums[shift_index]
                
                # Insert the value into its correctly sorted position
                nums[search_left_boundary] = value_to_insert

        # ---------------------------------------------------------------------
        # PHASE 2: MERGE SUBROUTINE
        # ---------------------------------------------------------------------
        def merge_adjacent_runs(left_start: int, middle_divider: int, right_end: int):
            """Combines two sorted adjacent segments: left chunk and right chunk."""
            # Create shallow temporary copies of the two segments to safely overwrite the original list
            left_temporary_copy = nums[left_start : middle_divider + 1]
            right_temporary_copy = nums[middle_divider + 1 : right_end + 1]
            
            left_pointer = 0
            right_pointer = 0
            merged_write_pointer = left_start
            
            # Compare elements from both copies and write the smaller one back to the main array
            while left_pointer < len(left_temporary_copy) and right_pointer < len(right_temporary_copy):
                if left_temporary_copy[left_pointer] <= right_temporary_copy[right_pointer]:
                    nums[merged_write_pointer] = left_temporary_copy[left_pointer]
                    left_pointer += 1
                else:
                    nums[merged_write_pointer] = right_temporary_copy[right_pointer]
                    right_pointer += 1
                merged_write_pointer += 1
                
            # If any elements remain in the left copy, drain them into the array
            while left_pointer < len(left_temporary_copy):
                nums[merged_write_pointer] = left_temporary_copy[left_pointer]
                left_pointer += 1
                merged_write_pointer += 1
                
            # If any elements remain in the right copy, drain them into the array
            while right_pointer < len(right_temporary_copy):
                nums[merged_write_pointer] = right_temporary_copy[right_pointer]
                right_pointer += 1
                merged_write_pointer += 1

        # ---------------------------------------------------------------------
        # EXECUTION: STEP 1 - Build the Initial Sorted Runs
        # ---------------------------------------------------------------------
        # Iterate through the array in chunks of TARGET_RUN_SIZE and sort them individually
        for run_start_index in range(0, total_elements, TARGET_RUN_SIZE):
            run_end_index = min(run_start_index + TARGET_RUN_SIZE - 1, total_elements - 1)
            binary_insertion_sort(run_start_index, run_end_index)
            
        # ---------------------------------------------------------------------
        # EXECUTION: STEP 2 - Merge the Runs Together
        # ---------------------------------------------------------------------
        # Start combining pairs of runs. We begin with size=32, then size=64, size=128, etc.
        current_merge_size = TARGET_RUN_SIZE
        while current_merge_size < total_elements:
            
            # Walk through the entire array merging neighboring pairs of the current size
            for left_boundary in range(0, total_elements, 2 * current_merge_size):
                
                # Determine the exact boundaries for the two segments to be merged
                middle_boundary = min(left_boundary + current_merge_size - 1, total_elements - 1)
                right_boundary = min(left_boundary + (2 * current_merge_size) - 1, total_elements - 1)
                
                # Only perform a merge if a valid secondary right segment actually exists
                if middle_boundary < right_boundary:
                    merge_adjacent_runs(left_boundary, middle_boundary, right_boundary)
                    
            # Double the merge size threshold for the next pass
            current_merge_size *= 2
            
        return nums
