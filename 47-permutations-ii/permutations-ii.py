class Solution:
    def solve(self, index, nums, result):
        if index == len(nums):
            result.append(nums.copy())
            return
        used = set()   
        for i in range(index, len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            self.solve(index + 1, nums, result)
            nums[index], nums[i] = nums[i], nums[index]

    def permuteUnique(self, nums):
        result = []
        nums.sort()              
        self.solve(0, nums, result)
        return result
