class Solution:
    def lowerbound(self,nums,target):
        n=len(nums)
        lb=-1
        low=0
        high=n-1
        while high>=low:
            mid=(low+high)//2
            if(nums[mid]>=target):
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb


    def upperbound(self,nums,target):
        n=len(nums)
        ub=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]>target):
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound=self.lowerbound(nums,target)
        if(lower_bound==-1 or nums[lower_bound] != target):
            return[-1,-1]
        upper_bound=self.upperbound(nums,target)
        return[lower_bound,upper_bound-1]
# from typing import List

# class Solution:
#     def lowerbound(self, nums, target):
#         n = len(nums)
#         lb = -1
#         low, high = 0, n - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] >= target:
#                 lb = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return lb

#     def upperbound(self, nums, target):
#         n = len(nums)
#         ub = n   # <-- fix here
#         low, high = 0, n - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] > target:
#                 ub = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return ub

#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         lower_bound = self.lowerbound(nums, target)
#         if lower_bound == -1 or nums[lower_bound] != target:
#             return [-1, -1]   # <-- list not tuple
#         upper_bound = self.upperbound(nums, target)
#         return [lower_bound, upper_bound - 1]
        