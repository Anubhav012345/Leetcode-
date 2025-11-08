class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        add=0
        multiply=1
        while n!=0:
            remainder=n%10
            add+=remainder
            multiply*=remainder
            n=n//10
        ans=add+multiply
        if(ans==0):
            return False
        return (original%ans==0)
        