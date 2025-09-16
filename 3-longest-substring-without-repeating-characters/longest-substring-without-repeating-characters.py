class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash_map={}
        # ans=0
        # n=len(s)
        # for i in range(n):
        #     if(s[i] in hash_map):
        #         ans=max(ans,len(hash_map))
        #     else:
        #         hash_map[s[i]]=1
        # return ans
                
        ans=0
        n=len(s)
        for i in range(n):
            hash_map={}
            for j in range(i,n):
                if s[j] in hash_map:
                    break
                hash_map[s[j]]=1
                ans=max(ans,len(hash_map))
        return ans

        