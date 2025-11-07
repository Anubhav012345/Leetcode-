class Solution:
    def gcd(self,odd_sum,even_sum):
        while even_sum:
            odd_sum,even_sum=even_sum,odd_sum%even_sum
        return odd_sum
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum=n*n
        even_sum=n*(n+1)
        ans=self.gcd(odd_sum,even_sum)
        return ans