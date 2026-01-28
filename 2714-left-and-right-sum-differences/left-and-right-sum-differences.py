class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            left_sum=sum(nums[:i])
            right_sum=sum(nums[i+1:])
            ans.append(abs(left_sum-right_sum))
        return ans

        