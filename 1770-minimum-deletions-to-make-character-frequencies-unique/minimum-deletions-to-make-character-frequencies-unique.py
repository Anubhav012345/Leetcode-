class Solution:
    def minDeletions(self, s: str) -> int:
        hash_map={}
        for i in range (len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        
        sorted_hash_map=sorted(hash_map.values(),reverse=True)

        seen=set()
        ans=0
       
        for f in sorted_hash_map:
            while f > 0 and f in seen:
                f -= 1
                ans += 1
            seen.add(f)
        
        return ans