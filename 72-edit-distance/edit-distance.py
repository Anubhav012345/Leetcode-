class Solution:
    def dp_fn(self,i,j,str1,str2,dp):
        if(i<0):
            return j+1
        if j<0:
            return i+1
        if dp[i][j]!=-1:
            return dp[i][j]
        if str1[i]==str2[j]:
            return self.dp_fn(i-1,j-1,str1,str2,dp)
        dp[i][j]=min(1+self.dp_fn(i-1,j,str1,str2,dp),1+self.dp_fn(i,j-1,str1,str2,dp),1+self.dp_fn(i-1,j-1,str1,str2,dp))
        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1) for _ in range(n+1)]
        return self.dp_fn(n-1,m-1,word1,word2,dp)