class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_map={}
        for c in s:
            hash_map[c]=hash_map.get(c,0)+1
        for c in t:
            if c not in hash_map:
                return False
            hash_map[c]-=1
            if hash_map[c]<0:
                return False
        return True


            
        