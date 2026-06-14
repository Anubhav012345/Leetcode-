class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        nsum,sqsum=0,0
        while(n!=0):
            rem=n%10
            nsum+=rem
            sqsum+=rem*rem
            n//=10
        return sqsum-nsum>=50
        