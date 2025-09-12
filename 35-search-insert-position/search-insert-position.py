class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        lower_bound=n
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]>=target):
                lower_bound=mid
                high=mid-1
            else:
                low=mid+1
        return lower_bound

        