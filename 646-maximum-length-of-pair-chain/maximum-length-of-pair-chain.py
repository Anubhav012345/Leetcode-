class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n=len(pairs)
        memo={}
        ans=0
        for i in range(n):
            ans=max(ans,self.solve(i,n,pairs,memo))
        return ans

    def solve(self,x,n,pairs,memo):
        if x in memo:
            return memo[x]
        temp_ans=0
        for j in range(x+1,n):
            if(pairs[x][1]<pairs[j][0]):
                temp_ans=max(temp_ans,self.solve(j,n,pairs,memo))
        memo[x]=1+temp_ans
        return 1+temp_ans
        