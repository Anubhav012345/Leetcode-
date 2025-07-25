class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        a=x
        if x<0:
            return False
        while x>0:
            rev=x%10
            sum=sum*10+rev
            x=x//10
        if(sum==a):
            return True
        else:
            return False


        