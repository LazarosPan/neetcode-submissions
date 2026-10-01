class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        for i in reversed(range(len(arr))):
            current = arr[i]
            arr[i] = max_right	
            max_right = max(max_right, current)

        return arr
