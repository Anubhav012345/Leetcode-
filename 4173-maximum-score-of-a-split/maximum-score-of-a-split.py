class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = sum(nums) - nums[n - 1]
        suffixMin = nums[n - 1]

        result = -10 ** 15

        for i in reversed(range(n - 1)):
            result = max(result, prefixSum - suffixMin)
            prefixSum -= nums[i]
            suffixMin = min(suffixMin, nums[i])

        return result