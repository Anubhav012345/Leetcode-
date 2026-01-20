class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even=0
        for i in range(len(nums)):
            if(nums[i]%2==0):
                even+=1
                if(even>=2):
                    return True
                    break
        return False