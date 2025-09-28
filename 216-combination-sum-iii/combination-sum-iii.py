class Solution:
    def solve(self,last,total,subset,k,n,result):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        if len(subset)>k or total>n:
            return
        for i in range(last,10):
            sum=total+i
            subset.append(i)
            self.solve(i+1,sum,subset,k,n,result)
            subset.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.solve(1,0,[],k,n,result)
        return result