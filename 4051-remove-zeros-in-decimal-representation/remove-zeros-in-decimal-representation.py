class Solution:
    def removeZeros(self, n: int) -> int:
        stack=[]
        while n!=0:
            remainder=n%10
            n=n//10
            if remainder!=0:
                stack.append(remainder)
        m=0
        while stack:
            e=stack.pop()
            m=(m*10)+e
        return m


        
        