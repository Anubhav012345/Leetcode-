class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float("inf")]*(n+1)
        dp[0]=0
        for x in range(1,n+1):
            i=1
            while(i*i<=x):
                dp[x]=min(dp[x],1+dp[x-(i*i)])
                i+=1
        return dp[n]
        