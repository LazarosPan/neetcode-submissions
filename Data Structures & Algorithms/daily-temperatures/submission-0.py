class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Return the number of days until a warmer temperature for each day.

        Uses a monotonic decreasing stack of indices. Each index stays in
        the stack until a warmer temperature is found.

        Time: O(n)
        Space: O(n)
        """
        result = [0] * len(temperatures)
        stack = []  # Indices of days waiting for a warmer temperature

        for i in range(len(temperatures)):

            # Resolve all previous days colder than the current day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i

            # Current day now waits for a warmer temperature
            stack.append(i)

        return result