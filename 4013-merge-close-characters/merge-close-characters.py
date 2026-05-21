class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res=[]
        freq=[-1]*26
        for i in range(len(s)):
            ch=s[i];
            curr=(ord(ch)-ord('a'))
            if(freq[curr]!=-1 and len(res)-freq[curr]<=k):
                continue
            freq[curr]=len(res)
            res.append(ch)
        return "".join(res)