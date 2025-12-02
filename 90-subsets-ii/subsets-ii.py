class Solution:
    def solve(self, index, n, nums, subset):
        if index >= n:
            return [subset.copy()]      
        results = []
        subset.append(nums[index])
        results += self.solve(index + 1, n, nums, subset)
        subset.pop()
        while index + 1 < n and nums[index] == nums[index + 1]:
            index += 1
        results += self.solve(index + 1, n, nums, subset)
        return results
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.solve(0, len(nums), nums, [])
