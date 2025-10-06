class Solution:
    def alternateDigitSum(self, n: int) -> int:
        odd_sum=0
        even_sum=0
        digits=[int(d) for d in str(n)]
        for i in range(0,len(digits)):
            if i%2==0:
                even_sum+=digits[i]
            else:
                odd_sum+=digits[i]
        ans=even_sum-odd_sum
        return ans

        