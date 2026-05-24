class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i<j:
            if(nums[i]==0 and nums[j]!=0):
                count+=1
                nums[i],nums[j]=nums[j],nums[i]
            if(nums[i]!=0):
                i+=1
            if(nums[j]==0):
                j-=1
                
        return count
                
        