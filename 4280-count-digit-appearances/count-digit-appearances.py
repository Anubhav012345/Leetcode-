class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        b = 0
        for i in nums:
            a = str(i)
            b += a.count(str(digit))
        return b