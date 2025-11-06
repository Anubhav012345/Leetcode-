class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        if not tasks:
            return 0
        ans=float("inf")
        for s,t in tasks:
            ans=min(ans,s+t)
        return ans
        