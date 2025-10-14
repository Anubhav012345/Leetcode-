class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if(n<2*k):
            return False
        a=0
        while a+2*k<=n:
            b=a+k
            lst1=[]
            lst1[:]=nums[a:b]
            c=b+k
            lst2=[]
            lst2[:]=nums[b:c]
            increasing=True
            for i in range(k-1):
                j=i+1
                if(lst1[j]<=lst1[i]) or (lst2[j]<=lst2[i]):
                    increasing=False
                    break
            if increasing:
                return True
            a+=1
        return False
        