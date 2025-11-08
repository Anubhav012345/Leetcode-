class Solution:
    def maxProduct(self, n: int) -> int:
        lst=[]
        while n!=0:
            value=n%10
            lst.append(value)
            n//=10
        lst.sort()
        return(lst[-1]*lst[-2])
        
        