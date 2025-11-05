class Solution:
    def makeFancyString(self, s: str) -> str:
        st=''
        for i in range(len(s)):
            if(len(st)>=2 and st[len(st)-2]==st[len(st)-1] and st[len(st)-1]==s[i]):
                continue
            st+=s[i]
        return st

        