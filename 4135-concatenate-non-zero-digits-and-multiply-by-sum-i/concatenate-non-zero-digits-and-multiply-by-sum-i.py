class Solution:
    def sumAndMultiply(self, n: int) -> int:
        lst=[]
        digit=0
        while n!=0:
            rem=n%10
            if(rem!=0):
                lst.append(rem)
            n//=10
        add=sum(lst)
        lst.reverse()
        for i in range(len(lst)):
            digit=(digit*10+lst[i])
        return(digit*add)



        
        