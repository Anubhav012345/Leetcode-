class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_map={}
        hash_map1={}
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        
        for j in range(len(t)):
            hash_map1[t[j]]=hash_map1.get(t[j],0)+1
        
        ans=0
        for key,value in hash_map.items():
            ans+=max(0,value-hash_map1.get(key,0))
        return ans


        