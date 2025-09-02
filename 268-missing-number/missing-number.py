class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for i in range(0,n+1):
            freq[i]=0
        for num in nums:
            freq[num]=1
        for k,v in freq.items():
            if v==0:
                return k

        # Brute Force
        # n=len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
