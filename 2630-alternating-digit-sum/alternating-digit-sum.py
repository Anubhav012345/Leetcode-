class Solution:
    def alternateDigitSum(self, n: int) -> int:
        even_sum=0
        digits=[int(d) for d in str(n)]
        for i in range(0,len(digits)):
            if i%2==0:
                even_sum+=digits[i]
            else:
                even_sum-=digits[i]
        return even_sum

        