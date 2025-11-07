class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg=sum(nums)//len(nums)
        i=max(0, avg) + 1
        while i in nums:
            i+=1
        return i