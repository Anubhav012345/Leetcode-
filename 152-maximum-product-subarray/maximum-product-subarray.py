class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        
        for num in nums[1:]:
            # If num is negative, swapping helps because negative * min might become max
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            
            result = max(result, curr_max)
        
        return result
