class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while(mid<=high):
            if(nums[mid]==0):
                temp=nums[low]
                nums[low]=nums[mid]
                nums[mid]=temp
                mid+=1
                low+=1
            elif(nums[mid]==1):
                mid+=1
            else:
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high]=temp
                high-=1
        

        