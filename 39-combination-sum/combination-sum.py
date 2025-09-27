class Solution:
    def solve(self,index,total,subset,candidates,target,result):
        if index>=len(candidates):
            return
        if total==target:
            result.append(subset.copy())
            return
        elif(target<total):
            return
        subset.append(candidates[index])
        sum1=total+candidates[index]
        self.solve(index,sum1,subset,candidates,target,result)
        e=subset.pop()
        sum1-=e
        self.solve(index+1,total,subset,candidates,target,result)        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result

        