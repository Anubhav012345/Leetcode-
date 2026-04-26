class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        ans=[]
        mx=0
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
                ans.append(i)

        mx=0
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>mx:
                mx=nums[i]
                ans.append(i)
        ans=list(set(ans))
        ans.sort()
        res=[]
        for i in ans:
            res.append(nums[i])

        return res
                