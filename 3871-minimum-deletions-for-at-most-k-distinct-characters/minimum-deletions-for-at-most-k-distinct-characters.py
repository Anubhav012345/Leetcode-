class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        hash_map={}
        for i in range(len(s)):
            hash_map[s[i]]=hash_map.get(s[i],0)+1
        lst=[]
        for key,val in hash_map.items():
            lst.append(val)
        lst.sort(reverse=True)
        if len(lst)<0:
            return 0
        deletion=sum(lst[k:])
        return deletion