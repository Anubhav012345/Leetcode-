class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a=0
        for ch in s:
            if(ch=='a'):
                count_a+=1
        
        ans=count_a
        count_b=0

        for ch in s:
            if(ch=='a'):
                count_a-=1
            else:
                count_b+=1        
            ans=min( ans , count_a + count_b)
        
        return ans