class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                nums=nums[i:]+nums[:i]
                if(nums==sorted(nums)):
                    return len(nums)-i
                else:
                    return -1

        return 0

        
        



        