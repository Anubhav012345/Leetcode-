class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            x=i
            add=0
            while 0<x:
                rem=x%10
                add+=rem
                x//=10
            if(add%2==0):
                count+=1
        return count
        


        