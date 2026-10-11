class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # integer array heights
        # heights[i] represents the height of the ith bar
        # choose 2 bars that return the max height
        # do we know the width? distance between containers.

        # we want to find the indices that give the max width but also the highest containers so we max width*height

        # two pointers, one in the start one in the end, so we start from the max width
        # but we have to go all the way inside to check the height of all the containers as they still might give us better volume overall
        # do we need to store everything? no only the max volume found so far, with the indices that give this
        # if a list is empty we have to return 0 i suppose, before start iterating

        # formula that we want : volume(start,end) = (end-start) * min(heights[start],heights[end]) # width*height

        # Start with maximum possible width.
        # After computing the area:
        # - Move the pointer with the smaller height.
        # - Moving the taller height cannot help because the smaller
        #   height is the bottleneck and width would only decrease.
        
        if not heights:
            return 0
        
        start = 0
        end = len(heights)-1
        max_volume = 0

        while start < end: # if its equal we just return 0 volume as the start-end=0
            volume = (end-start) * min(heights[start],heights[end])
            if volume > max_volume: # is there a point to add the equal sign here as well? both work
                max_volume = volume
                
            if heights[start]<heights[end]: # again what if they are equal? both work
                start += 1
            else:
                end -=1
        
        return max_volume
