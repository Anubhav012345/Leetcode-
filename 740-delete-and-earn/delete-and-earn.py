class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        max_value=max(nums)
        freq=[0]*(max_value+1)
        for num in nums:
            freq[num] += num
        dp=[0]*(max_value+1)

        for i in range(max_value+1):
            dp[i]=max(dp[i-1],freq[i]+dp[i-2])
        
        return max(dp)