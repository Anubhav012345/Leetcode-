class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        last_smaller=float("-inf")
        largest=0
        for i in range(n):
            num=nums[i]
            if num-1==last_smaller:
                count+=1
                last_smaller=num
            elif(num!=last_smaller):
                last_smaller=num
                count=1
            largest=max(largest,count)
        return largest

        