class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n=len(nums)-1
        maxi=abs(nums[0]-nums[n])

        for i in range(n):
            maxi=max(maxi,abs(nums[i+1]-nums[i]))
        return maxi