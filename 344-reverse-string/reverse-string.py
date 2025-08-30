class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        self.func(s,left,right)
        
    def func(self,s,left,right):
        if left>=right:
            return
        s[left],s[right]=s[right],s[left]
        self.func(s,left+1,right-1)
        