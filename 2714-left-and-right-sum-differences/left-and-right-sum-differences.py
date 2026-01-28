class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        left=0
        right=sum(nums)

        for num in nums:
            res=abs(left-(right-num))
            ans.append(res)
            left+=num
            right-=num
        return ans


        