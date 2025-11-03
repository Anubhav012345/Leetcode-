class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num1=min(nums)
        num2=max(nums)
        lst=[]
        for i in range(num1,num2):
            if i not in nums:
                lst.append(i)
        return lst
            

        