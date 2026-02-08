class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        sumation=sum(nums)
        count=0
        while i < len(nums):
            sumation-=nums[i]     
            if n-1>0:           
                avg=sumation/(n - 1)
                if nums[i]>avg:
                    count+=1
            n-=1
            i+=1

        return count
