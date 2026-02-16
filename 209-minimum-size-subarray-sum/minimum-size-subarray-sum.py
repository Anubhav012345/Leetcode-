class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_len=float("inf")
        add=0

        for right in range(len(nums)):
            add+=nums[right]

            while(add>=target):
                min_len=min(min_len, right - left + 1)
                add-=nums[left]
                left+=1    
        
        if(min_len!=float("inf")):
            return min_len
        
        return 0
