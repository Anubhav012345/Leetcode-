class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True

        lst=[]
        while num>0:
            lst.append(num%10)
            num//=10
        lst.reverse()
        
        
        
        if(lst[-1]==0):
            return False
        return True
        