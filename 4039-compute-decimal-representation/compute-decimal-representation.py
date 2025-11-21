class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result=[]
        count=0
        while n!=0:
            rem=n%10
            mul=10**count
            result.append(rem*mul)
            n//=10
            count+=1
        result.reverse()
        ans=[]
        for i in range(len(result)):
            if result[i]!=0:
                ans.append(result[i])
        return ans
