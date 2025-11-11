class Solution:
    def minOperations(self, nums: List[int]) -> int:
        set1=set(nums)
        nums1=list(set1)
        if(len(nums1)==1):
            return 0
        return 1
        