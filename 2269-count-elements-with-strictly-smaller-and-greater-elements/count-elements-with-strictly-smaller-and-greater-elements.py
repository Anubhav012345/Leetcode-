class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)):
            if(nums[0]==nums[i] or nums[-1]==nums[i]):
                continue
            count+=1
        return count
        