class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lst=[0]*n
        pos=0
        neg=1
        for i in range(len(nums)):
            if(nums[i]>0):
                lst[pos]=nums[i]
                pos+=2
            else:
                lst[neg]=nums[i]
                neg+=2
        return lst




        