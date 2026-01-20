class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n=len(nums)-1

        if(nums[0]<nums[n]):
            for i in range(len(nums)-1):
                if(nums[i]>nums[i+1]):
                    return False
        else:
            for i in range(len(nums)-1):
                if(nums[i]<nums[i+1]):
                    return False
        
        return True
            


        