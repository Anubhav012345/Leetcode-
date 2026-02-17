class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n=len(values)
        memo={}

        def solve(i,j):

            if(i,j) in memo:
                return memo[(i,j)]
            
            if( j - i < 2 ):
                return 0
            
            ans=float("inf")

            for k in range(i+1,j):

                ans=min(ans,solve(i,k)+solve(k,j)+values[i]*values[k]*values[j])

            memo[(i,j)]=ans
            return ans
        
        return solve(0,n-1)

        