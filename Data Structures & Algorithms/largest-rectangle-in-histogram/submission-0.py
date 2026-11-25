class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)

        for i, height in enumerate(heights):
            start = i

            # Current height ends all taller rectangles.
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_area = max(max_area, h * (i - index))
                start = index

            stack.append((start, height))

        # Remaining rectangles extend to the end.
        n = len(heights)
        for index, h in stack:
            max_area = max(max_area, h * (n - index))

        return max_area