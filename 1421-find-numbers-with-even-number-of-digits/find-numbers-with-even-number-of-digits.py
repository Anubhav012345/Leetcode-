class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count=0

        for i in range(len(nums)):
            total=0
            x=nums[i]
            
            while 0<x:
                total+=1
                x//=10
            
            if(total%2==0):
                count+=1
            
        return count
        
        