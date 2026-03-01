class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        add= 0
        n = len(nums)
        for i in range(n):
            start = max(0, i-nums[i])
            add+= sum(nums[start: i+1])
        return add