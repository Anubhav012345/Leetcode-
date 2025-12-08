from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map=OrderedDict()
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        for key,value in hash_map.items():
            if value == 1:
                return s.index(key)
        return -1
