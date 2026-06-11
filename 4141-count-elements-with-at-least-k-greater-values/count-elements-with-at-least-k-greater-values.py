class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(nums)
            
        nums.sort()
        n = len(nums)

        threshold = nums[n - k]

        ans = 0
        for x in nums:
            if x < threshold:
                ans += 1

        return ans