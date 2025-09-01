class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst=[]
        i=0
        while i<len(nums):
            if(nums[i]!=0):
                i+=1
            else:
                lst.append(nums.pop(i))
        return(nums.extend(lst))