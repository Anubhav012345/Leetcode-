class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = sum(nums[:3])
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                s = nums[i] + nums[i + 1] + nums[i + 2]
                if abs(s - target) < abs(closest - target):
                    closest = s
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < target:
                s = nums[i] + nums[n - 2] + nums[n - 1]
                if abs(s - target) < abs(closest - target):
                    closest = s
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return closest