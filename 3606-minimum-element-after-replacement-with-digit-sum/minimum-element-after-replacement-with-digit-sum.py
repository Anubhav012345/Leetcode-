class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini=float("inf")
        for i in range(len(nums)):
            x=nums[i]
            num=0
            while x>0:
                rem=x%10
                num+=rem
                x//=10
            
            mini=min(mini,num)
        return mini
        