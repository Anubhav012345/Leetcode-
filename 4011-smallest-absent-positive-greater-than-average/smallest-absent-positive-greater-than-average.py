class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            if(nums[0]>=0):
                return nums[0]+1
            else:
                return 1
        else:
            x=sum(nums)/n
            if x<0:
                ans=1
                while ans in nums:
                    ans+=1
                return ans
            ans=int(x)+1
            while ans in nums:
                ans+=1
            return ans
        