class Solution:
    def func(self,n):
        if n<=1:
            return n
        return(self.func(n-1)+self.func(n-2))
    def fib(self, n: int) -> int:
        ans=self.func(n)
        return ans