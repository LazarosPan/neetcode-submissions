from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        get = groups.get

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - 97] += 1

            key = tuple(count)

            group = get(key)

            if group is None:
                groups[key] = [word]
            else:
                group.append(word)

        return list(groups.values())