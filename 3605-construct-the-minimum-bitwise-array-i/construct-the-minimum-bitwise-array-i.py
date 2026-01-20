class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        lst=[-1]*n
        while i<n:
            for j in range(0,nums[i]):
                if((j | (j+1))==nums[i]):
                    lst[i]=j
                    break
            i+=1
        return lst
        