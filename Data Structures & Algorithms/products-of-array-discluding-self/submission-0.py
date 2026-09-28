class Solution:
    def productExceptSelf(self, numbers: List[int]) -> List[int]:
        # Create a result list with the same length as numbers.
        #
        # If numbers = [1, 2, 4, 6], then:
        # [1] * 4 becomes [1, 1, 1, 1]
        #
        # We use 1 because 1 is the neutral value for multiplication:
        # 1 * any_number = any_number
        products_except_self = [1] * len(numbers)

        # Stores the product of all numbers located before the current index.
        # At index 0, there are no numbers to the left, so we start with 1.
        product_to_the_left = 1

        # Move from left to right:
        # index values will be 0, 1, 2, 3
        for index in range(len(numbers)):
            # Store the product of everything to the left of this index.
            products_except_self[index] = product_to_the_left

            # Include the current number for the next index.
            product_to_the_left *= numbers[index]

        # At this point, for [1, 2, 4, 6]:
        # products_except_self = [1, 1, 2, 8]

        # Stores the product of all numbers located after the current index.
        # At the last index, there are no numbers to the right,
        # so we start with 1 again.
        product_to_the_right = 1

        # Move backward through the indexes.
        #
        # range(start, stop, step)
        # start = len(numbers) - 1, which is the last valid index
        # stop  = -1, but -1 itself is NOT included
        # step  = -1, meaning subtract 1 each time
        #
        # For a list of length 4, this produces:
        # 3, 2, 1, 0
        for index in reversed(range(len(numbers))):
            # The result already contains the product to the left.
            # Multiply it by the product to the right.
            products_except_self[index] *= product_to_the_right

            # Include the current number for the next index to the left.
            product_to_the_right *= numbers[index]

        return products_except_self