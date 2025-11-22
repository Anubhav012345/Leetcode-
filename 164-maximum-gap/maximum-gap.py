class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if(len(nums)<=1):
            return 0
        nums.sort()
        maxi=float("-inf")
        for i in range(len(nums)-1):
            j=i+1
            ans=nums[j]-nums[i]
            maxi=max(maxi,ans)
        return maxi

        