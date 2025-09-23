class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(index,subset):
            if index>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            solve(index+1,subset)
            subset.pop()
            solve(index+1,subset)
        solve(0,[])
        return res