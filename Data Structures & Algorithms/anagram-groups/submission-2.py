from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = bytearray(26)

            for char in word:
                count[ord(char) - 97] += 1

            key = bytes(count)
            group = groups.get(key)

            if group is None:
                groups[key] = [word]
            else:
                group.append(word)

        return list(groups.values())