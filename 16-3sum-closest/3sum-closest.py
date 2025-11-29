class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lst=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                add_ele=nums[i]+nums[j]+nums[k]
                lst.append(add_ele)
                if add_ele < target:
                    j += 1
                else:
                    k -= 1
        closet = lst[0]
        min_diff = abs(closet - target)
        for x in lst:
            diff = abs(x - target)
            if diff < min_diff:
                min_diff = diff
                closet = x
        return closet
