class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_min=float("inf")
        second_min=float("inf")

        for i in range(1,len(nums)):
            if(nums[i]<first_min):
                second_min=first_min
                first_min=nums[i]
            elif(first_min <= nums[i] and nums[i] < second_min):
                second_min=nums[i]
        
        ans=nums[0]+first_min+second_min
        return ans
        