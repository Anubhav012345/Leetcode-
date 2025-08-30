class Solution:
    def func(self,x,left,right):
        if(int(x)<0):
            return False
        if(left>=right):
            return True
        if(x[left]!=x[right]):
            return False
        return self.func(x,left+1,right-1)
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        left=0
        right=len(x)-1
        return self.func(x,left,right)



        