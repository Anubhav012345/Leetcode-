class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=len(nums)-1

        while i<j:
            add_num=str(nums[i])+str(nums[j])
            ans+=int(add_num)
            i+=1
            j-=1
        
        if(i==j):
            ans+=nums[i]
        
        return ans

        