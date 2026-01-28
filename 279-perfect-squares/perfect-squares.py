class Solution:
    def numSquares(self, n: int) -> int:
        memo={}
        def solve(n):
            if n==0:
                return 0
            if n in memo:
                return memo[n]
            ans=float("inf")
            i=1
            while(i*i<=n):
                ans=min(ans,1+solve(n-(i*i)))
                i+=1
            memo[n]=ans
            return ans
        return solve(n)
        