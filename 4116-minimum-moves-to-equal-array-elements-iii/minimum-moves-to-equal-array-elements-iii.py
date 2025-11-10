class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        result=0
        for i in range(len(nums)):
            ans=maxi-nums[i]
            result+=ans
        return result
        