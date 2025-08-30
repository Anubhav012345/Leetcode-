class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0, len(s), 2 * k):
            left=i
            right=min(i+k-1,len(s)-1)
            self.func(s, left, right)
        return(''.join(s))
    def func(self,s,left,right):
        if left>=right:
            return
        s[left],s[right]=s[right],s[left]
        self.func(s,left+1,right-1)
        