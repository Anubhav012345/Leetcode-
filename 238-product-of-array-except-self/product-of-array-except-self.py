class Solution:
    def product(self,list1,list2):
        multiply1=1
        for i in range(len(list1)):
            multiply1=multiply1*list1[i]
        
        for i in range(len(list2)):
            multiply1=multiply1*list2[i]
        
        return multiply1

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        for i in range(len(nums)):
            mul=mul*nums[i]
        
        lst=[0]*len(nums)
        for i in range(len(nums)):
            if(mul==0):
                if(nums[i]==0):
                    ans=self.product(nums[:i],nums[i+1:])
                    lst[i]=ans
            else:
                lst[i]=int(mul/nums[i])
        
        return lst

        