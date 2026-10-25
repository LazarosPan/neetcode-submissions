from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return [[""]]

        # print(strs)
        # strs.sort()
        # print(strs)

        result = defaultdict(list) # mapping char count to list of anagrams

        for string in strs:
            count = [0] * 26 # a ... z

            for char in string:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(string)
        
        return list(result.values())