class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        max_value=max(nums)
        freq=[0]*(max_value+1)
        for num in nums:
            freq[num] += num
        memo={}

        def solve(i):
            if(i>max_value):
                return 0
            if(i in memo):
                return memo[i]
            skip=solve(i+1)
            take=freq[i]+solve(i+2)
            memo[i]=max(skip,take)

            return max(skip,take)
        
        return solve(1)