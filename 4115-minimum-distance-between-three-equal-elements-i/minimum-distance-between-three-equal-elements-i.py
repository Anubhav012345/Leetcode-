class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        result=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=len(nums)-1
                while k>j:
                    if(nums[i]==nums[j]==nums[k]):
                        ans=abs(i-j)+abs(j-k)+abs(k-i)
                        result=min(ans,result)
                    k-=1

        if(result!=float('inf')):
            return result
        return -1
        