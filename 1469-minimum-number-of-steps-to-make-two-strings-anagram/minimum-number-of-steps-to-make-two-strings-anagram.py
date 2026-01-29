class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_map={}
        hash_map1={}
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        
        for j in range(len(t)):
            hash_map1[t[j]]=hash_map1.get(t[j],0)+1
        
        ans=0
        for key1,value1 in hash_map.items():
            for key,value in hash_map1.items():
                if(key1==key):
                    if(value1>value):
                        ans+=(value1-value)
                    break
            else:
                ans+=value1
        return ans


        