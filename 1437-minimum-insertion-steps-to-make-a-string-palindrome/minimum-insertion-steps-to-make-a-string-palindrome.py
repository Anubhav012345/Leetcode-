class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        memo={}
        def solve(i,j):
            if i>=j:
                return 0
            if(i,j) in memo:
                return memo[(i,j)]
            if(s[i]==s[j]):
                return solve(i+1,j-1)
            else:
                ans= 1+min((solve(i,j-1)),(solve(i+1,j)))
            
            memo[(i,j)]=ans
            return ans
        
        return solve(0,n-1)