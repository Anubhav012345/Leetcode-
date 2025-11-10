class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hash_map={}
        count=0
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        for k in hash_map.items():
            count+=1
        return count
        
        