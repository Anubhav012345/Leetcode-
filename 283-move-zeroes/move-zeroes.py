class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst=[]

        for i in range(len(nums)):
            if(nums[i]!=0):
                lst.append(nums[i])

        n=len(nums)
        m=len(lst)
        for i in range(m,n):
            lst.append(0)    
        
        for i in range(n):
            nums[i]=lst[i]