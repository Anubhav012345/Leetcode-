class Solution:
    def rotateElements(self, nums, k):
        a=[x for x in nums if x>=0]
        m=len(a)
        if m==0:
            return nums
        k%=m
        j=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=a[(j+k)%m]
                j+=1
        return nums