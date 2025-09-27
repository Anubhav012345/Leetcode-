class Solution:
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset.copy())
            return
        if total>target:
            return
        if len(nums)<=index:
            return
        subset.append(nums[index])
        sum1=total+nums[index]
        self.solve(index+1,sum1,subset,nums,target,result)
        e=subset.pop()
        sum1-=e
        next_index=index+1
        while next_index<len(nums) and nums[index]==nums[next_index]:
            next_index+=1
        self.solve(next_index,sum1,subset,nums,target,result)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result

        