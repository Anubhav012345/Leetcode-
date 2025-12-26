class Solution:
    def mirrorDistance(self, n: int) -> int:
        actual_num=n
        num=''
        while n>0:
            rem=n%10
            num=num+str(rem)
            n//=10
        reverse_num=int(num)
        return(abs(reverse_num-actual_num))
