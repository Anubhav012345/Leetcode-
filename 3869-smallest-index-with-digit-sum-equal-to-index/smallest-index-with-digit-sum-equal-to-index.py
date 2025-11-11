class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            add=0
            num=nums[i]
            while num>0:
                rem=num%10
                add+=rem
                num//=10
            if(add==i):
                return i
        return -1


        