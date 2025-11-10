class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for x in nums:
            ans+=nums[-1]-x
        return ans
        