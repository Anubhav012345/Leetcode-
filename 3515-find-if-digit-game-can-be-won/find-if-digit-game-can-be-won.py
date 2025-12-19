class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        add_num=sum(nums)
        
        single_digit=0
        for i in range(len(nums)):
            if(nums[i]>=10):
                break
            single_digit+=nums[i]
        
        double_digit=add_num-single_digit
        
        if(double_digit==single_digit):
            return False
        return True
        