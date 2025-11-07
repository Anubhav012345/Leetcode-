class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        total=sum(nums)
        odd_sum=0
        for i in range(1,len(nums),2):
            odd_sum+=nums[i]
        even_sum=total-odd_sum
        return(even_sum-odd_sum)

        