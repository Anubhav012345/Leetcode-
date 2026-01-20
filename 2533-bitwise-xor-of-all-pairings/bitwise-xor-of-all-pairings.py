class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result=0

        if(len(nums2)%2==1):
            for i in range(len(nums1)):
                result^=nums1[i]

        if(len(nums1)%2!=0):
            for i in range(len(nums2)):
                result^=nums2[i]
            
        return result
