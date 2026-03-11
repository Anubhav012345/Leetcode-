class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map={}

        for ch in range(len(s)):
            hash_map[s[ch]]=hash_map.get(s[ch],0)+1

        for key,value in hash_map.items():
            if(value==1):
                return s.index(key)
        return -1
        