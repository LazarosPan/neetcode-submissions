class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        start = 0
        end = len(heights)-1
        max_volume = 0

        while start < end:
            volume = (end-start)*min(heights[start], heights[end])
            max_volume = max(volume, max_volume)
            
            if heights[start]<heights[end]:
                start += 1
            else:
                end -= 1
        return max_volume