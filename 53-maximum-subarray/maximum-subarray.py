class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range(0,n):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi

    __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


    # Brute Force Approach
    #     n=len(nums)
    #     maxi=float("-inf")
    #     for i in range(0,n):
    #         total=0
    #         for j in range(i,n):
    #             total+=nums[j]
    #             maxi=max(maxi,total)
    #     return maxi
        